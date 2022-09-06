import logging
from .const import LIGHTWAVE_LINK2, LIGHTWAVE_ENTITIES, SERVICE_SETBRIGHTNESS, CONF_HOMEKIT
from homeassistant.components.light import LightEntity
from homeassistant.components.light import (
    ATTR_BRIGHTNESS, COLOR_MODE_BRIGHTNESS, COLOR_MODE_RGB)
from homeassistant.core import callback
from homeassistant.helpers import entity_platform, entity_registry
from homeassistant.helpers.entity import EntityCategory
from .const import DOMAIN

DEPENDENCIES = ['lightwave2']
_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Find and return LightWave lights."""

    lights = []
    link = hass.data[DOMAIN][config_entry.entry_id][LIGHTWAVE_LINK2]

    homekit = config_entry.options.get(CONF_HOMEKIT, False)
    if not homekit:
        for featureset_id, name in link.get_lights():
            lights.append(LWRF2Light(name, featureset_id, link, hass))
    else:
        er = entity_registry.async_get(hass)
        for featureset_id, name in link.get_lights():
            if entity_id := er.async_get_entity_id('light', DOMAIN, featureset_id):
                _LOGGER.debug("Removing entity provided by Homekit %s", entity_id)
                er.async_remove(entity_id)

    for featureset_id, name in link.get_lights():
        if link.featuresets[featureset_id].has_led():
            lights.append(LWRF2LED(name, featureset_id, link, hass))

    for featureset_id, name in link.get_hubs():
        if link.featuresets[featureset_id].has_led():
            lights.append(LWRF2LED(name, featureset_id, link, hass))

    async def service_handle_brightness(light, call):
        _LOGGER.debug("Received service call set brightness %s", light._name)
        brightness = int(round(call.data.get("brightness") / 255 * 100))
        feature_id = link.featuresets[light._featureset_id].features['dimLevel'].id
        await link.async_write_feature(feature_id, brightness)

    platform = entity_platform.async_get_current_platform()
    platform.async_register_entity_service(SERVICE_SETBRIGHTNESS, None, service_handle_brightness, )

    hass.data[DOMAIN][config_entry.entry_id][LIGHTWAVE_ENTITIES].extend(lights)
    async_add_entities(lights)

class LWRF2Light(LightEntity):
    """Representation of a LightWaveRF light."""

    def __init__(self, name, featureset_id, link, hass):
        self._name = name
        self._hass = hass
        _LOGGER.debug("Adding light: %s ", self._name)
        self._featureset_id = featureset_id
        self._lwlink = link
        self._state = \
            self._lwlink.featuresets[self._featureset_id].features["switch"].state
        self._brightness = int(round(
            self._lwlink.featuresets[self._featureset_id].features["dimLevel"].state / 100 * 255))
        self._gen2 = self._lwlink.featuresets[self._featureset_id].is_gen2()
        self._has_led = self._lwlink.featuresets[self._featureset_id].has_led()
        for featureset_id, hubname in link.get_hubs():
            self._linkid = featureset_id

    async def async_added_to_hass(self):
        """Subscribe to events."""
        await self._lwlink.async_register_callback(self.async_update_callback)

    #TODO add async_will_remove_from_hass() to clean up

    @callback
    def async_update_callback(self, **kwargs):
        """Update the component's state."""
        if kwargs["feature"] == "uiButtonPair" and self._lwlink.get_featureset_by_featureid(kwargs["feature_id"]).featureset_id == self._featureset_id:
            _LOGGER.debug("Button (light) press event: %s %s", self.entity_id, kwargs["new_value"])
            self._hass.bus.fire("lightwave2.click",{"entity_id": self.entity_id, "code": kwargs["new_value"]},
        )
        self.async_schedule_update_ha_state(True)

    @property
    def supported_color_modes(self):
        """Flag supported features."""
        return {COLOR_MODE_BRIGHTNESS}

    @property
    def color_mode(self):
        """Flag supported features."""
        return COLOR_MODE_BRIGHTNESS

    @property
    def should_poll(self):
        """Lightwave2 library will push state, no polling needed"""
        return False

    @property
    def assumed_state(self):
        """Gen 2 devices will report state changes, gen 1 doesn't"""
        return not self._gen2

    async def async_update(self):
        """Update state"""
        self._state = \
            self._lwlink.featuresets[self._featureset_id].features["switch"].state
        self._brightness = int(round(
            self._lwlink.featuresets[self._featureset_id].features["dimLevel"].state / 100 * 255))

    @property
    def name(self):
        """Lightwave switch name."""
        return self._name

    @property
    def brightness(self):
        """Return the brightness of the group lights."""
        return self._brightness

    @property
    def unique_id(self):
        """Unique identifier. Provided by hub."""
        return self._featureset_id

    @property
    def is_on(self):
        """Lightwave switch is on state."""
        return self._state

    async def async_turn_on(self, **kwargs):
        """Turn the LightWave light on."""
        _LOGGER.debug("HA light.turn_on received, kwargs: %s", kwargs)

        if ATTR_BRIGHTNESS in kwargs:
            _LOGGER.debug("Changing brightness from %s to %s (%s%%)", self._brightness, kwargs[ATTR_BRIGHTNESS], int(kwargs[ATTR_BRIGHTNESS] / 255 * 100))
            self._brightness = kwargs[ATTR_BRIGHTNESS]
            await self._lwlink.async_set_brightness_by_featureset_id(
                self._featureset_id, int(round(self._brightness / 255 * 100)))

        self._state = True
        await self._lwlink.async_turn_on_by_featureset_id(self._featureset_id)

        self.async_schedule_update_ha_state()

    async def async_turn_off(self, **kwargs):
        """Turn the LightWave light off."""
        _LOGGER.debug("HA light.turn_off received, kwargs: %s", kwargs)

        self._state = False
        await self._lwlink.async_turn_off_by_featureset_id(self._featureset_id)
        self.async_schedule_update_ha_state()

    async def async_set_rgb(self, led_rgb):
        await self._lwlink.async_set_led_rgb_by_featureset_id(self._featureset_id, led_rgb)

    @property
    def extra_state_attributes(self):
        """Return the optional state attributes."""

        attribs = {}

        for featurename, feature in self._lwlink.featuresets[self._featureset_id].features.items():
            attribs['lwrf_' + featurename] = feature.state

        attribs['lrwf_product_code'] = self._lwlink.featuresets[self._featureset_id].product_code

        return attribs

    @property
    def device_info(self):
        return {
            'identifiers': { (DOMAIN, self._featureset_id) },
            'name': self.name,
            'manufacturer': "Lightwave RF",
            'model': self._lwlink.featuresets[self._featureset_id].product_code,
            'via_device': (DOMAIN, self._linkid)
        }

class LWRF2LED(LightEntity):
    """Representation of a LightWaveRF LED."""

    def __init__(self, name, featureset_id, link, hass):
        self._name = f"{name} LED"
        self._device = name
        self._hass = hass
        _LOGGER.debug("Adding LED: %s ", self._name)
        self._featureset_id = featureset_id
        self._lwlink = link
        color = \
            self._lwlink.featuresets[self._featureset_id].features["rgbColor"].state
        if color == 0:
            self._state = False
            self._r = 255
            self._g = 255
            self._b = 255
        else:
            self._state = True
            self._r = color // 65536
            self._g = (color - self._r * 65536) // 256
            self._b = (color - self._r * 65536 - self._g * 256)
        self._brightness = max(self._r, self._g, self._b)
        self._r = int(self._r * 255 / self._brightness)
        self._g = int(self._g * 255 / self._brightness)
        self._b = int(self._b * 255 / self._brightness)
        self._gen2 = self._lwlink.featuresets[self._featureset_id].is_gen2()
        for featureset_id, hubname in link.get_hubs():
            self._linkid = featureset_id

    async def async_added_to_hass(self):
        """Subscribe to events."""
        await self._lwlink.async_register_callback(self.async_update_callback)

    #TODO add async_will_remove_from_hass() to clean up

    @callback
    def async_update_callback(self, **kwargs):
        """Update the component's state."""
        self.async_schedule_update_ha_state(True)

    @property
    def supported_color_modes(self):
        """Flag supported features."""
        return {COLOR_MODE_RGB}

    @property
    def color_mode(self):
        """Flag supported features."""
        return COLOR_MODE_RGB

    @property
    def should_poll(self):
        """Lightwave2 library will push state, no polling needed"""
        return False

    @property
    def assumed_state(self):
        """Gen 2 devices will report state changes, gen 1 doesn't"""
        return not self._gen2

    @property
    def entity_category(self):
        return EntityCategory.CONFIG

    async def async_update(self):
        """Update state"""
        color = \
            self._lwlink.featuresets[self._featureset_id].features["rgbColor"].state
        if color == 0:
            self._state = False
        else:
            self._state = True
            self._r = color // 65536
            self._g = (color - self._r * 65536) //256
            self._b = (color - self._r * 65536 - self._g * 256)
            self._brightness = max(self._r, self._g, self._b)
            self._r = int(self._r * 255 / self._brightness)
            self._g = int(self._g * 255 / self._brightness)
            self._b = int(self._b * 255 / self._brightness)

    @property
    def name(self):
        """Lightwave switch name."""
        return self._name

    @property
    def brightness(self):
        """Return the brightness of the group lights."""
        return self._brightness

    @property
    def rgb_color(self):
        return (self._r, self._g, self._b)

    @property
    def unique_id(self):
        """Unique identifier. Provided by hub."""
        return f"{self._featureset_id}_LED"

    @property
    def is_on(self):
        """Lightwave switch is on state."""
        return self._state

    async def async_turn_on(self, **kwargs):
        """Turn the LightWave light on."""
        _LOGGER.debug("HA led.turn_on received, kwargs: %s", kwargs)

        self._state = True
        if 'rgb_color' in kwargs:
            self._r = kwargs['rgb_color'][0]
            self._g = kwargs['rgb_color'][1]
            self._b = kwargs['rgb_color'][2]
        
        if 'brightness' in kwargs:
            self._brightness = kwargs['brightness']

        r = int(self._r * self._brightness /255)
        g = int(self._g * self._brightness /255)
        b = int(self._b * self._brightness /255)
        rgb = r * 65536 + g * 256 + b

        await self._lwlink.async_set_led_rgb_by_featureset_id(self._featureset_id, rgb)

        self.async_schedule_update_ha_state()

    async def async_turn_off(self, **kwargs):
        """Turn the LightWave light off."""
        _LOGGER.debug("HA light.turn_off received, kwargs: %s", kwargs)
        self._state = False
        await self._lwlink.async_set_led_rgb_by_featureset_id(self._featureset_id, 0)

        self.async_schedule_update_ha_state()

    @property
    def extra_state_attributes(self):
        """Return the optional state attributes."""

        attribs = {}

        for featurename, feature in self._lwlink.featuresets[self._featureset_id].features.items():
            attribs['lwrf_' + featurename] = feature.state

        return attribs

    @property
    def device_info(self):
        return {
            'identifiers': { (DOMAIN, self._featureset_id) },
            'name': self._device,
            'manufacturer': "Lightwave RF",
            'model': self._lwlink.featuresets[self._featureset_id].product_code,
            'via_device': (DOMAIN, self._linkid)
        }
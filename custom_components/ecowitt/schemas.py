"""Schema definitions"""
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from .const import (
    CONF_UNIT_BARO,
    CONF_UNIT_WIND,
    CONF_UNIT_RAIN,
    CONF_UNIT_WINDCHILL,
    CONF_UNIT_LIGHTNING,
    CONF_NAME,
    DEFAULT_PORT,
    DOMAIN,
    W_TYPE_HYBRID,
)
from homeassistant.const import (
    CONF_PORT,
    CONF_UNIT_SYSTEM_METRIC,
    CONF_UNIT_SYSTEM_IMPERIAL,
)

COMPONENT_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_PORT): cv.port,
        vol.Optional(CONF_UNIT_BARO,
                     default=CONF_UNIT_SYSTEM_METRIC): cv.string,
        vol.Optional(CONF_UNIT_WIND,
                     default=CONF_UNIT_SYSTEM_IMPERIAL): cv.string,
        vol.Optional(CONF_UNIT_RAIN,
                     default=CONF_UNIT_SYSTEM_IMPERIAL): cv.string,
        vol.Optional(CONF_UNIT_LIGHTNING,
                     default=CONF_UNIT_SYSTEM_IMPERIAL): cv.string,
        vol.Optional(CONF_UNIT_WINDCHILL,
                     default=W_TYPE_HYBRID): cv.string,
    }
)

CONFIG_SCHEMA = vol.Schema({DOMAIN: COMPONENT_SCHEMA}, extra=vol.ALLOW_EXTRA)

DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_PORT, default=DEFAULT_PORT): cv.port,
        vol.Optional(CONF_NAME,
                     description={"suggested_value": "ecowitt"}): str,
    }
)

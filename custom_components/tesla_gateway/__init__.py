"""
Monitors and controls the Tesla gateway.
"""
import logging

import asyncio
import voluptuous as vol
import teslapy

from homeassistant.const import (
    CONF_USERNAME,
    CONF_PASSWORD
    )
import homeassistant.helpers.config_validation as cv

DOMAIN = 'tesla_gateway'

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_USERNAME): cv.string,
        vol.Required(CONF_PASSWORD): cv.string
    }),
}, extra=vol.ALLOW_EXTRA)

@asyncio.coroutine
def async_setup(hass, config):

    domain_config = config[DOMAIN]
    conf_user = domain_config[CONF_USERNAME]
    conf_password = domain_config[CONF_PASSWORD]
    
    tesla = teslapy.Tesla(domain_config[CONF_USERNAME])

    def get_battery():
        batteries = tesla.battery_list()
        if len(batteries) > 0:
            return batteries[0]
        else:
            return None

    @asyncio.coroutine
    async def set_operation(service):
        
        battery = await hass.async_add_executor_job(get_battery)
        if not battery:
            _LOGGER.warning('Battery object is None')
            return None

        await hass.async_add_executor_job(battery.set_operation, service.data['real_mode'])
        if 'backup_reserve_percent' in service.data:
            await hass.async_add_executor_job(battery.set_backup_reserve_percent, service.data['backup_reserve_percent'])

    hass.services.async_register(DOMAIN, 'set_operation', set_operation)

    @asyncio.coroutine
    async def set_reserve(service):
        
        battery = await hass.async_add_executor_job(get_battery)
        if not battery:
            _LOGGER.warning('Battery object is None')
            return None
            
        if 'backup_reserve_percent' in service.data:
            await hass.async_add_executor_job(battery.set_backup_reserve_percent, service.data['backup_reserve_percent'])

    hass.services.async_register(DOMAIN, 'set_reserve', set_reserve)

    return True

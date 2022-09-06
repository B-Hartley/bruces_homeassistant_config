# Home Assistant Configuration

This is the Home Assistant configuration I've put together over the last year or so.
The config file is split into a large number of [packages](packages) to allow it to be browsed and reused more easily.
I'm doing my best to document each section so you can see what it is doing.

Most config files are in the [packages](packages) directory.  So browse around in there !

If you want to, you can.....<a href="https://www.buymeacoffee.com/Qc5YIVJLHe" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

Main features are:

* [Floorplan](lovelace/floorplan/) with lights / radiators / temperatures / presence - entity types can be switched on and off.<br>[<img src="documents/images/floor_plan_all.jpg" width=100>](documents/images/floor_plan_all.jpg)[<img src="documents/images/floorplan_switches.jpg" width=100>](documents/images/floorplan_switches.jpg)
* [Remote Control](/lovelace/lounge-remote/) for Lounge AV equipment (SkyQ, Denon AV, Philips TV including Ambilight + Hue)<br>[<img src="documents/images/lounge_remote_navigation_off.jpg" width=100>](documents/images/lounge_remote_navigation_off.jpg)[<img src="documents/images/lounge_remote_navigation.jpg" width=100>](documents/images/lounge_remote_navigation.jpg)[<img src="documents/images/lounge_remote_channels.jpg" width=100>](documents/images/lounge_remote_channels.jpg)[<img src="documents/images/lounge_remote_numbers.jpg" width=100>](documents/images/lounge_remote_numbers.jpg)[<img src="documents/images/lounge_remote_appletv.jpg" width=100>](documents/images/lounge_remote_appletv.jpg)
* Room Level Presence using [room-assistant](packages/systems/room-assistant/) on several Raspberry Pi Zeros.
* [Hot Tub](packages/areas/garden) scheduling and monitoring and Octopus Agile/Go pricing optimisation for Balboa (and La-Z-Spa)
* [Cat Litter Tray monitoring](packages/systems/litter_trays) (using Flic buttons to track usage/cleaning and alert when cleaning required)<br>[<img src="documents/images/litter_trays.jpg" width=100>](documents/images/litter_trays.jpg)
* [Texecom Elite Intruder Alarm](packages/systems/texecom_alarm/) System via MQTT (gives access to movement sensors and door sensors as well as alarm status (incl. arming/disarming)
* Cost optimised charging of [Powerwall](packages/systems/tesla_powerwall) and [EVs](packages/systems/myenergi) for Octopus Agile/Go TOU Electric Tarrif with [Solar Forecasting](https://forecast.solar/).
* [Telegram Bot](packages/systems/telegram/) integration to allow status reporting and control of some house features from telegram messenge with free text or commands.
* [Unifi Protect](packages/systems/unifi-protect/) Cameras inside and outside the house with person and vehicle detection outside.
* [Deepstack](https://deepstack.cc/) AI Server on [Jetson Nano](https://developer.nvidia.com/embedded/jetson-nano-developer-kit) - Face and Object recongnition
* Control from Alexa or Siri, using Alexa integration & HomeKit
* Big and Easy to Use Phone Menu<br><img src="documents/images/phone_menu.jpg" width=100>
## [Hardware List](documents/hardwareList.md)
## [Add-ons, integrations and custom components](documents/HA_integrations_and_addons.md)
## [Helpers Created through UI](documents/helpers.md)




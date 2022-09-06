# Texecom Elite Intruder Alarm

I use [Texecom2MQTT](https://github.com/dchesterton/texecom2mqtt-hassio) add on to link my Intruder Alarm panel into home assistant.
It exposes motion sensors and door sensors to Home Assistant, it also passes arm / disarm and allows the system to be armed and disarmed.
It also passes log information which allows capture of users when they enter their codes or present their tags.

One automation is triggered by a status change of the alarm, this handles:
* Critical alert message for alarm triggered
* Lights off when setting at night
* Logbook of Arm, Disarm
* Updating device trackers for Cleaner / Cat Sitter etc.

Another automation keeps track of most recent person to arrive.

If authorised user is at home when front or back door are opened when alarm is armed it will disarm and notify.


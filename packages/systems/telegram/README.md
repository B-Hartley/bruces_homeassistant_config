# Telegram Bot

Uses the Telegram Bot (Webhooks) integration to send notifications and allow 'chat' with the house.
Can send plan text requests or /commands.

Following commands are available:
* /help - lists commands available
* /status - shows status of house (alarm, doors, devices left on, cars etc.)
* /alarm - Shows alarm status and offers keyboard to arm alarm (various modes)
* /camera - send stills from CCTV cameras
* /hottub - shows status of hottub and offers keyboard to manage temp changes / schedule changes etc.
* /jyggy - status and keybaord to control of charging on our Tesla Model S
* /paddy - status and keybaord to control of charging on our Renault Zoe

Following Free Text requests are available:
* help
* status
* alarm "disarm alarm", "alarm arm", " alarm arm night", "alarm home" etc.
* paddy
* jyggy
* picture / camera
* video
* hottub "hot tub 09:00", "hot tub 38c", "set tub to 38c for 16:00"

Following command callbacks are executed by in-line keyboards:
* /remove_keyboard
* /paddy_refresh
* /paddy_<charge mode>
* /jyggy_refresh
* /jyggy_<charge mode>
* /arm_away /arm_home /arm_night /disarm
* /30m /1h /3h - defer a message for a time
* /tub_sched_on|off
* /tub_set_time
* /tub_time_08 etc.
* /tub_set_temp
* /tub_temp_38 etc.
* /video
  
  

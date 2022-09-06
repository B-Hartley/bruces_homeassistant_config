# Litter Trays

Cat Litter Tray monitoring with Flic Buttons

* A Flic button on each tray
* Click once if clearing a wee from the tray
* Double click if clearing a poo from the tray
* Long press if fully cleaning the tray

The system then monitors when was the last full clean and how many wees and poos have been cleaned out.
When tray reaches a certain level of dirty, a telegram message is sent asking us to clean the tray.

## Flic Button Configuration

### Single Click:
* URL: https://mydomain.example.com/api/events/flic
* Content-Type: application/json
* Body: {"type":"littertray","button_name":"tray_drum","click_type":"wee"}
* Header: Authorization: Bearer xxxxxxxxxxxxxxxxx

### Double Click:
* URL: https://mydomain.example.com/api/events/flic
* Content-Type: application/json
* Body: {"type":"littertray","button_name":"tray_drum","click_type":"poo"}
* Header: Authorization: Bearer xxxxxxxxxxxxxxxxx

### Hold:
* URL: https://mydomain.example.com/api/events/flic
* Content-Type: application/json
* Body: {"type":"littertray","button_name":"tray_drum","click_type":"reset"}
* Header: Authorization: Bearer xxxxxxxxxxxxxxxxx

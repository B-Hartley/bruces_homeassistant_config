# Smart Meters

* Electric Meter [Kaifa MA120](https://zigbeealliance.org/zigbee_products/kaifa-ma120-single-phase-electricity-meter-2/)
* Gas Meter

The electric and gas meters are connected to a [Hildebrand IHD/CAD](https://www.hildebrand.co.uk/our-products/display/).
This takes live data from the Smart meters through the Secure Zigbee PAN.
This is then made available through an API and an MQTT server.
This provides live usage and also historical info and meter readings.

The Hildebrand MQTT Server is bridged into my local MQTT server so I can obtain the data from this and other services.

To bridge MQTT, firstly setup the MQTT add-on in Home Assistant like this:

```
logins:
  - username: XXXXXX
    password: XXXXXX
anonymous: false
customize:
  active: true
  folder: mosquitto
certfile: fullchain.pem
keyfile: privkey.pem
require_certificate: false
```

in share/mosquitto create a file
glowmqtt.conf

```
connection glowmqtt
  address glowmqtt.energyhive.com:8883
  topic SMART/HILD/XXXXXXXXXXXX in 0
  try_private false
  notifications true
  start_type automatic
  remote_clientid glow
  remote_username xxxxxxxxx
  remote_password xxxxxxxxx
  keepalive_interval 300
  cleansession true
  bridge_protocol_version mqttv311
  local_clientid homeassistant
  bridge_cafile /etc/ssl/certs/ca-certificates.crt
```

create another file:
accesscontrollist.txt

```
user XXXXXXXX
topic readwrite #
```

final file:
acl_file
```
acl_file /share/mosquitto/accesscontrollist
```

Data is in Zigbee Smart Energy Format:

```
0702: Metering
- 00: Reading Information Set
 - 00: CurrentSummationDelivered: energy consumed (meter)
 - 01: CurrentSummationReceived: solar panels production?
 - 02: CurrentMaxDemandDelivered: ?
 - 07: ReadingSnapshotTime: UTC time
 - 14: Supply Status: 0x2 is on
- 02: Meter Status
- 03: Formatting
- 04: Historical Consumption
 - 00: InstantaneousDemand (Signed)
 - 01: CurrentDayConsumptionDelivered
 - 30: CurrentWeekConsumptionDelivered
 - 40: CurrentMonthConsumptionDelivered
0705: Prepayment
0708: Device Management
```

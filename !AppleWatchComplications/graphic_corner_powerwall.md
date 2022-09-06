# Powerwall

## Graphic Corner

* Template: Gauge Text
* Show When Locked: True
* Leading: 
```
{{ states('input_number.powerwall_reserve_requested') }}
```
* Outer: 
```
{{ ((states('sensor.powerwall_charge')|float(0) * 1.05)-5.0)|int(0)}}%
{% if is_state('binary_sensor.powerwall_charging','on') %}➕{% endif %}
```
* Trailing: 
```
100
```
* Gauge: 
```
{{ ((((states('sensor.powerwall_charge')|float(0) *1.05)-5.0) -
states('input_number.powerwall_reserve_requested')|float(0) ) ) / 
(100.0 - states('input_number.powerwall_reserve_requested')|float(0))}}
```
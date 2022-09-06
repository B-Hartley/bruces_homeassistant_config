# Home Consumption

## Graphic Corner

* Template: Gauge Text
* Show When Locked: True

* Leading: 
```
0
```
* Outer: 
```
🏠{{ states('sensor.floorplan_powerwall_home_load')|float(0)|round(1)}}
```
* Trailing: 
```
{% if states('sensor.floorplan_powerwall_home_load')|float(0) < 8.5 %}8{% else %}18{% endif %}
```
* Gauge: 
```
{% if states('sensor.floorplan_powerwall_home_load')|float(0) < 8.5 
%}{{ [states('sensor.floorplan_powerwall_home_load')|float(0) / 8.0,1]|min}}{% 
else %}{{ [states('sensor.floorplan_powerwall_home_load')|float(0) / 18.0,1]|min}}{% endif %}
```
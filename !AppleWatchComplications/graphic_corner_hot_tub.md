# Hot Tub

## Graphic Corner

* Template: Gauge Text
* Show When Locked: True

* Leading: 
```
{{ [states('sensor.hottub_water_temp')|float(0),28]|min }}
```
* Outer: 
```
{% if is_state('sensor.hottub_summary','offline') %}🚫{% endif %}{% 
if is_state('switch.spa_light1','on') %}💡{% endif %}{%
if is_state('fan.spa_pump1','on') or is_state('fan.spa_pump2','on') %}✈️{% endif %}{%
if is_state('input_boolean.hottub_scheduled','on') %}⏱{% endif %}{%
if state_attr('climate.spa_climate','hvac_action') == 'heating' %}🔥{% endif %}{%
if is_state('binary_sensor.spa_filter1','on') %}♻️{% endif %}
{% if is_state('switch.spa_light1','off') and is_state('fan.spa_pump1','off') and is_state('fan.spa_pump2','off') and is_state('input_boolean.hottub_scheduled','off') and 
state_attr('climate.spa_climate','hvac_action') != 'heating'and is_state('binary_sensor.spa_filter1','off') %}{{ states('input_number.hottub_water_temp') }}{% endif %}


```
* Trailing: 
```
{{ states('input_number.hottub_water_target')|int(0) }} 
```
* Gauge: 
```
{% if states('input_number.hottub_water_temp')|float(0) > states('input_number.hottub_water_target')|float(0) %}1.0{%
else%}{{ (states('input_number.hottub_water_temp')|float(0) - 28.0 )/(states('input_number.hottub_water_target')|float(0) - 28.0)}}{%endif%}
```








## Graphic Corner

* Template: Gauge Text
* Show When Locked: True

* Leading: 
```
{{ [states*'sensor.hottub_water_temp')|int(0),28]|min }}
```
* Outer: 
```
{% if states('sensor.hottub_summary') == 'heating' %}🔥{% 
elif states('sensor.hottub_summary') == 'scheduled' %}⏱{% 
elif states('sensor.hottub_summary') == 'circulating' %}✅{% 
elif states('sensor.hottub_summary') == 'off' %}❄️{% 
endif %}{{ states('input_number.hottub_water_temp')|int(0)}}°c
```
* Trailing: 
```
{{ states('input_number.hottub_water_target')|int(0) }} 
```
* Gauge: 
```
{{ [(states('sensor.hottub_water_temp')|float(0) - [states*'sensor.hottub_water_temp')|int(0),28]|min ) /
(states('input_number.hottub_water_target')|float(0) - [states*'sensor.hottub_water_temp')|int(0),28]|min), 1]|min}} 
```










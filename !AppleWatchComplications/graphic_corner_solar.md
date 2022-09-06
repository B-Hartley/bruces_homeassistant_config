# Solar


Live production figure, Gauge shows daily forecast
## Graphic Corner

* Template: Gauge Text
* Show When Locked: True

* Leading: 
```
0
```
* Outer: 
```
{% if states('sun.sun') == 'below_horizon'%}{{ states('input_number.solcast_latest_today_forecast')|int(0) }}/{{ 
(states('sensor.forecastsolar_tomorrow')|float(0))|int(0) }}{% 
else %}☀️ {{ states('sensor.solar_production')|float(0) }}{% endif %}
```
* Trailing: 
```
{{ states('input_number.solcast_latest_today_forecast')|int(0) }}
```
* Gauge: 
```
{{[ (states('sensor.solar_production_daily_kw')|float(0)) / (states('input_number.solcast_latest_today_forecast')|float(0)) ,1]|min }}
```


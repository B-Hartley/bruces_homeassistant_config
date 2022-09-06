# Zigbee 

On Zigbee I have.....
* Aqara Door sensors
* Smart Plugs
* Environment Sensor (Temp / Humidity / CO2)

and Hue products that are not on the Hue Bridge
* Hue bulbs
* Hue Dimmers
* outdoor movement sensors
* indoor movements sensors

## Aqara Door sensors battery levels

This code simply takes the battery attribute of each sensor and exposes it as a template sensor so I can use it in my [floorplan](../../../lovelace/floorplan/).

eg.
```  
binary_sensor:
  - platform: template
    sensors:
      bar_door_low_battery:
        friendly_name: 'Bar Door - Low Battery'
        value_template: "{{ (states('sensor.bar_door_battery') | float) < 20.0 }}"
```        

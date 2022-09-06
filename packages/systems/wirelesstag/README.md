# Wireless Sensor Tags

I have a number of Tags from [wirelesstag.net](https://wirelesstag.net/)
I use them as gate opening sensors / temperature sensors etc.

As they are quite old they can't handle the authentication that is required to link them into home assistant.
So they pass through a [json-proxy](https://www.npmjs.com/package/json-proxy) on another machine that adds in the authentication headers.

I had to manually tweak the wireless tags component so that it programmes the tags with this alternate ip address.
I copied the wirelesstags folder into custom components, found the section where the ip is set and changed it.
Need to be aware that if any changes are made I have to merge them in.

```
{
  "server": {
    "port": 9321,
    "webroot": "$config_dir",
    "html5mode": "/index.html"
  },
  "proxy": {
    "forward": {
      "/api/": "http://xxx.xxx.xx.xxx:8123"
    },
    "headers": {
      "Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  }
}
```

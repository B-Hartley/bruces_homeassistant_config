# Solcast

Solar Forecasting service, free for personal use.
Did have automations to upload live info to allow "tuning" of the forecat.

Have switched to an overnight batch script, that downloads data from SolarEdge, reformats it and uploads it to SolCast:

```
import requests
import json
import datetime

yesterday_date =  str(datetime.date.today()+datetime.timedelta(days=-1))
url = 'https://monitoringapi.solaredge.com/site/XXXXXXX/energy?timeUnit=QUARTER_OF_AN_HOUR&endDate=' + yesterday_date + '&startDate=' + yesterday_date + '&api_key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
req = requests.get(url)

#json_file = './input.txt'
#json_filehandle=open(json_file,'r')
#json_object=json.load(json_file)
json_object = json.loads(req.text)
jsonObj = {"measurements": []}

dict = json_object['energy']['values']
for dateValue in dict:
    date_time_str = dateValue["date"]
    dateValue_value = dateValue["value"]
    if dateValue_value == None:
      dateValue_value = 0.0
    date_time_obj = datetime.datetime.strptime(date_time_str,'%Y-%m-%d %H:%M:%S')
    date_time_fifteen = date_time_obj + datetime.timedelta(minutes=15)
    periodDetails = {
        "period_end": date_time_fifteen.strftime('%Y-%m-%dT%H:%M:%S.000000+00:00'),
        "period": "PT15M",
        "total_power": round(dateValue_value*4.0/1000.0,3)
    }
    jsonObj["measurements"].append(periodDetails)

post_url='https://api.solcast.com.au/rooftop_sites/XXXX-XXXX-XXXX-XXXX/measurements'
headers = {'Authorization': 'Bearer XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
result=requests.post(post_url,json=jsonObj, headers=headers)

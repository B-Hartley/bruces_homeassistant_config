# Bin Day

A script running on a seperate pi scrapes the local council website.
It then places a json file onto a webserver for Home Assistant to pick up.

There is a REST sensor for each bin type that has details of the next collection.
The binary sensor allows them to be displayed on the [floorplan](../../../lovelace/floorplan/)

The script running elsewhere to scrape the data is run from a cron job.
This is based on a script from [robbrad](https://github.com/robbrad/UKBinCollectionData)
I've made a few minor changes to handles chases where bin types are missing.

```
#!/usr/bin/env python3
import requests
import re
import json
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}

url = 'https://forms.n-somerset.gov.uk/Waste/CollectionSchedule'
values = {'PreviousHouse' : '',
          'PreviousPostcode' : 'xxxx xxx',
          'Postcode' : 'xxxx xxx',
          'SelectedUprn' : '99999999' }

req = requests.post(url, values, headers=headers)

soup = BeautifulSoup(req.text, features="html.parser")

rows = soup.find("table", {'class': re.compile('table')}).find_all("tr")

#Form a JSON wrapper
data = {"Rubbish":[],"Recycling":[],"Garden":[],"Food":[]}

#Loops the Rows
for row in rows:
    cells = row.find_all("td")
    if cells: 
        binType = cells[0].get_text(strip=True)
        collectionDate = cells[1].get_text(strip=True)
        if len(cells) > 2:
            nextCollectionDate = cells[2].get_text(strip=True)
        else:
            nextCollectionDate = ''
        #Make each Bin element in the JSON
        dict_data = {
        "BinType": binType,
        "collectionDate": collectionDate,
        "nextCollectionDate": nextCollectionDate
        }

        #Add data to the main JSON Wrapper
        if binType=="Rubbish":
          data['Rubbish'].append(dict_data)
        elif binType=="Garden":
          data['Garden waste'].append(dict_data)
        elif binType=="Recycling":
          data['Recycling'].append(dict_data)
        elif binType=="Food":
          data['Food'].append(dict_data)

##Make the JSON
json_data = json.dumps(data,sort_keys=True, indent=4)

#Output the data - run this script with a redirect to send the output to a file
#Suggest Crontab
print(json_data)
```

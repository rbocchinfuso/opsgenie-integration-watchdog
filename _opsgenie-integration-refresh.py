#!/usr/bin/python
import sys
import json
import subprocess
import time
from urllib.request import urlopen
from opsgenie.swagger_client import AlertApi
from opsgenie.swagger_client import configuration
from opsgenie.swagger_client.models import *
from opsgenie.swagger_client.rest import ApiException

API_KEY = str(sys.argv[1])
#print (API_KEY)

opsgenieURL = "https://api.opsgenie.com/v2/integrations?apiKey=" + API_KEY
json_object = json.load(urlopen(opsgenieURL))
#print (json_object)

current_dict = {}
if json_object['data'] == []:
    print ('No Data!')
else:
    for rows in json_object['data']:
      name = str(rows['name'])
      enabled = str(rows['enabled'])
      current_dict.update ({name : enabled})
      #current_dict = ({name : enabled})
      #time.sleep(5)
with open('integrations.json', 'w') as file:
     file.write(json.dumps(current_dict))
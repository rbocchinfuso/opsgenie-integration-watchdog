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

def setup_opsgenie_client():
    configuration.api_key['Authorization'] = API_KEY
    configuration.api_key_prefix['Authorization'] = 'GenieKey'
    # Provides more detailed request
    # configuration.debug = True

def create_alert(cur_name,cur_value,control_value):
    setup_opsgenie_client()

    body = CreateAlertRequest(
        message='Integration ' + cur_name + ' enabled = ' + cur_value,
        alias=cur_name,
        description='OpsGenie ' + cur_name + ' integration enabled = ' + cur_value + ' | control set enabled = ' + control_value,
        teams=[TeamRecipient(name='quokka.one')],
        visible_to=[TeamRecipient(name='quokka.one', type='team')],
        actions=['ping', 'restart'],
        tags=['opsgenie', 'integration', 'operations', cur_name],
        entity='',
        priority='P1',
        user='noreply@quokka.one',
        note='Alert created')

    try:
        response = AlertApi().create_alert(body=body)

        print('request id: {}'.format(response.request_id))
        print('took: {}'.format(response.took))
        print('result: {}'.format(response.result))
    except ApiException as err:
        print("Exception when calling AlertApi->create_alert: %s\n" % err)


opsgenieURL = "https://api.opsgenie.com/v2/integrations?apiKey=" + API_KEY
json_object = json.load(urlopen(opsgenieURL))
#print (json_object)

# Ingest integrations.json into control_dict
with open('integrations.json') as integrations_json:
    integration_control = integrations_json.read()
    #print(integration_control)

control_dict = json.loads(integration_control)
#print (control_dict)
 
while 1:
  current_dict = {}
  if json_object['data'] == []:
      print ('No Data!')
  else:
      for rows in json_object['data']:
        name = str(rows['name'])
        enabled = str(rows['enabled'])
        current_dict.update ({name : enabled})
        #current_dict = ({name : enabled})
        #print (current_dict)
        #time.sleep(5)
  for key, value in current_dict.items():
    if key in current_dict and (current_dict[key] != control_dict[key]):
        print ('OpsGenie ' + key + ' integration enabled = ' + value + ' | control set enabled = ' + control_dict[key])
        create_alert(key,value,control_dict[key])
  print (current_dict)
  time.sleep(3600);      
  


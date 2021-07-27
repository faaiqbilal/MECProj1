from __future__ import print_function
import time
import swagger_client
from swagger_client.configuration import Configuration
import json
from swagger_client.rest import ApiException
from pprint import pprint


configuration = Configuration()
configuration.host = "https://try-mec.etsi.org/sbxkhy32c3/rni/v2"

# create an instance of the API class
api_instance = swagger_client.RniApi(swagger_client.ApiClient(configuration))
app_ins_id = ['10.10.0.1', '10.100.0.1'] # list[str] | Comma separated list of Application instance identifiers

body = {
  "subscriptionType": "CellChangeSubscription",
  "callbackReference": "/subscriptions/test1",
  "filterCriteriaAssocHo": {
    "associateId": [
      {
        "type": 1,
        "value": "10.100.0.1"
      }
    ],
    "ecgi": [
      {
        "plmn": {
          "mnc": "001",
          "mcc": "001"
        },
        "cellId": "1010101"
      }
    ]
  }
}

# api_response = api_instance.subscriptions_post(body)
# pprint(api_response)

# body = swagger_client.CellChangeSubscription(callback_reference="/rni/v2/subscriptions/test2")
# body = swagger_client.InlineSubscription()

subscription_id = 2
api_response = api_instance.subscriptions_delete(subscription_id)
pprint(api_response)

''' Working subscription code 

# api_response = api_instance.subscriptions_post(body) # this creates the subscription, and the one below it appears to work by subscription_id
# pprint(api_response)

subscription_id = 1
api_response = api_instance.subscriptions_get(subscription_id) # this works for now
pprint(api_response)

'''

# api_response = api_instance.subscriptions_post(body) # this creates the subscription, and the one below it appears to work by subscription_id
# pprint(api_response)


# subscription_id = 2
# api_response = api_instance.subscriptions_get(subscription_id) # this works for now
# pprint(api_response)


'''
# S1-U bearer information #

try:
    api_response = api_instance.s1_bearer_info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RniApi->s1_bearer_info_get: %s\n" % e)

'''

'''
# LAYER 2 INFO STUFF #

try:
    api_response_l2 = api_instance.layer2_meas_info_get(app_ins_id = app_ins_id)
    pprint(api_response_l2)
except ApiException as e:
    print("Exception when calling RniApi->layer2_meas_info_get: %s\n" % e)

'''

'''

# RAB INFO STUFF #
try:
    api_response = api_instance.rab_info_get() # returns RabInfo object
    api_response_dict = api_response.to_dict()
    cell_user_info = api_response_dict['cell_user_info']

    cell_id_list = []
    cell_associateid_val_list =  [] 
    cell_associateid_type_list = [] 
    cell_erab_id_list = []
    cell_erab_qci_list = []
    cell_erab_qos_info_list = []
    
    # extracting info from object
    for cell_info in cell_user_info:
        cell_ecgi = cell_info['ecgi']
        cell_ueinfo = cell_info['ue_info'] 
        cell_id = cell_ecgi['cell_id']  # save cell id
        cell_ueinfo_extract = cell_ueinfo[0] 
        cell_associateid = cell_ueinfo_extract['associate_id'] # identifier for cellular device (both type and id)
        cell_associateid_extract = cell_associateid[0] # changing datastructure (info nested in list)
        cell_associateid_val = cell_associateid_extract['value'] # label for the cellular device in question
        cell_associateid_type = cell_associateid_extract['type'] # checks if ipv4 or ipv6 etc
        cell_erab_info = cell_ueinfo_extract['erab_info'] 
        cell_erab_info_extract = cell_erab_info[0] # changing datastructure (info nested in list)
        cell_erab_id = cell_erab_info_extract['erab_id'] # keep for identification purposes
        cell_erab_qos_params = cell_erab_info_extract['erab_qos_parameters'] 
        cell_erab_qci = cell_erab_qos_params['qci'] # need to save this
        cell_erab_qos_info = cell_erab_qos_params['qos_information'] # save this info, probably can't make feature out of it though

        # adding info to the lists we have created
        # these lists will be sent to the sheets we will create
        cell_id_list.append(cell_id)
        cell_associateid_val_list.append(cell_associateid_val)
        cell_associateid_type_list.append(cell_associateid_type)
        cell_erab_id_list.append(cell_erab_id)
        cell_erab_qci_list.append(cell_erab_qci)
        cell_erab_qos_info_list.append(cell_erab_qos_info)
except ApiException as e:
    print("Exception when calling RniApi->rab_info_get: %s\n" % e)

'''
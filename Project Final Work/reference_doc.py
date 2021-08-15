from __future__ import print_function
import time
import swagger_client
from swagger_client.configuration import Configuration
import json
from swagger_client.rest import ApiException
from pprint import pprint


# Needed for the configuration of the Sandbox
# The configuration host is the 

configuration = Configuration()
configuration.host = "https://try-mec.etsi.org/sbxk90259d/rni/v2"

# create an instance of the API class
api_instance = swagger_client.RniApi(swagger_client.ApiClient(configuration))
app_ins_id = ['10.10.0.1', '10.100.0.1'] # list[str] | Comma separated list of Application instance identifiers

# for now it seems that body structure is best off made like this, the functions dedicated to them can also be used but require the
# same information to be passed in as variables anyway, this appears to be more convenient
# Disregarding performance difference, it might take longer to process strings but that doesn't really matter for our use + no way to test


# callbackreference needs to be changed
# Cell Change Subscription body

cell_change_body = {
  "subscriptionType": "CellChangeSubscription",
  "callbackReference": "http://185.233.18.22",
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
        "cellId": "2020202"
      }
    ]
  }
}

# RAB establishment subscription body

rab_est_body = {
  "subscriptionType": "RabEstSubscription",
  "callbackReference": "http://my.callback.com/rni/rabEst",
  "filterCriteriaQci": {
    "ecgi": [
      {
        "plmn": {
          "mnc": "001",
          "mcc": "001"
        },
        "cellId": "1010101"
      }
    ],
    "qci": 80
  }
}

# api_response = api_instance.subscriptions_post(cell_change_body)
# pprint(api_response)

# api_response = api_instance.subscriptions_post(rab_est_body)
# pprint(api_response)


'''
New Radio Measurement Report (5g only)

# Nr Measurement Report ue Subscription body

filter_criteria_nr_mrs = {
  "associateId": [
      {
        "type": 1,
        "value": "10.100.0.1"
      }
    ]
  }


nr_meas_sub_body = swagger_client.NrMeasRepUeSubscription(callback_reference="anything", filter_criteria_nr_mrs=filter_criteria_nr_mrs, subscription_type="NrMeasRepUeSubscription")

api_response = api_instance.subscriptions_post(nr_meas_sub_body)
pprint(api_response)

'''

'''
Measurement Report (4g+5g) Subscription Request

# change the value to add another device to the list
filter_criteria_assoc_tri = {
  "associateId": [
      {
        "type": 1,
        "value": "10.100.0.1"
      }
    ]
  }


meas_sub_body = swagger_client.MeasRepUeSubscription(callback_reference="anything2", filter_criteria_assoc_tri=filter_criteria_assoc_tri, subscription_type="MeasRepUeSubscription")

api_response = api_instance.subscriptions_post(meas_sub_body)
pprint(api_response)

'''


'''

# Subscription Delete Code
# In this case, the subscription id is an ID that is returned as the last part of the URI chosen by the API (the part after the final '/')

api_response = api_instance.subscriptions_delete(subscription_id=1)
pprint(api_response)

'''

''' Working subscription code 

# api_response = api_instance.subscriptions_post(body) # this creates the subscription, and the one below it appears to work by subscription_id
# pprint(api_response)

subscription_id = 1
api_response = api_instance.subscriptions_get(subscription_id) # this works for now
pprint(api_response)

'''


# api_response = api_instance.subscriptions_post(body) # this creates the subscription, and the one below it appears to work by subscription_id
# pprint(api_response)

# subscription_id = '3' # parsed as string, regardless of whether it is entered as int or str
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
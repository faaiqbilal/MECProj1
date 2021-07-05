# swagger_client.RniApi

All URIs are relative to *https://localhost/rni/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**layer2_meas_info_get**](RniApi.md#layer2_meas_info_get) | **GET** /queries/layer2_meas | Retrieve information on layer 2 measurements
[**plmn_info_get**](RniApi.md#plmn_info_get) | **GET** /queries/plmn_info | Retrieve information on the underlying Mobile Network that the MEC application is associated to
[**rab_info_get**](RniApi.md#rab_info_get) | **GET** /queries/rab_info | Retrieve information on Radio Access Bearers
[**s1_bearer_info_get**](RniApi.md#s1_bearer_info_get) | **GET** /queries/s1_bearer_info | Retrieve S1-U bearer information related to specific UE(s)
[**subscription_link_list_subscriptions_get**](RniApi.md#subscription_link_list_subscriptions_get) | **GET** /subscriptions | Retrieve information on subscriptions for notifications
[**subscriptions_delete**](RniApi.md#subscriptions_delete) | **DELETE** /subscriptions/{subscriptionId} | Cancel an existing subscription
[**subscriptions_get**](RniApi.md#subscriptions_get) | **GET** /subscriptions/{subscriptionId} | Retrieve information on current specific subscription
[**subscriptions_post**](RniApi.md#subscriptions_post) | **POST** /subscriptions | Create a new subscription
[**subscriptions_put**](RniApi.md#subscriptions_put) | **PUT** /subscriptions/{subscriptionId} | Modify an existing subscription

# **layer2_meas_info_get**
> L2Meas layer2_meas_info_get(app_ins_id=app_ins_id, cell_id=cell_id, ue_ipv4_address=ue_ipv4_address, ue_ipv6_address=ue_ipv6_address, nated_ip_address=nated_ip_address, gtp_teid=gtp_teid, dl_gbr_prb_usage_cell=dl_gbr_prb_usage_cell, ul_gbr_prb_usage_cell=ul_gbr_prb_usage_cell, dl_nongbr_prb_usage_cell=dl_nongbr_prb_usage_cell, ul_nongbr_prb_usage_cell=ul_nongbr_prb_usage_cell, dl_total_prb_usage_cell=dl_total_prb_usage_cell, ul_total_prb_usage_cell=ul_total_prb_usage_cell, received_dedicated_preambles_cell=received_dedicated_preambles_cell, received_randomly_selected_preambles_low_range_cell=received_randomly_selected_preambles_low_range_cell, received_randomly_selected_preambles_high_range_cell=received_randomly_selected_preambles_high_range_cell, number_of_active_ue_dl_gbr_cell=number_of_active_ue_dl_gbr_cell, number_of_active_ue_ul_gbr_cell=number_of_active_ue_ul_gbr_cell, number_of_active_ue_dl_nongbr_cell=number_of_active_ue_dl_nongbr_cell, number_of_active_ue_ul_nongbr_cell=number_of_active_ue_ul_nongbr_cell, dl_gbr_pdr_cell=dl_gbr_pdr_cell, ul_gbr_pdr_cell=ul_gbr_pdr_cell, dl_nongbr_pdr_cell=dl_nongbr_pdr_cell, ul_nongbr_pdr_cell=ul_nongbr_pdr_cell, dl_gbr_delay_ue=dl_gbr_delay_ue, ul_gbr_delay_ue=ul_gbr_delay_ue, dl_nongbr_delay_ue=dl_nongbr_delay_ue, ul_nongbr_delay_ue=ul_nongbr_delay_ue, dl_gbr_pdr_ue=dl_gbr_pdr_ue, ul_gbr_pdr_ue=ul_gbr_pdr_ue, dl_nongbr_pdr_ue=dl_nongbr_pdr_ue, ul_nongbr_pdr_ue=ul_nongbr_pdr_ue, dl_gbr_throughput_ue=dl_gbr_throughput_ue, ul_gbr_throughput_ue=ul_gbr_throughput_ue, dl_nongbr_throughput_ue=dl_nongbr_throughput_ue, ul_nongbr_throughput_ue=ul_nongbr_throughput_ue, dl_gbr_data_volume_ue=dl_gbr_data_volume_ue, ul_gbr_data_volume_ue=ul_gbr_data_volume_ue, dl_nongbr_data_volume_ue=dl_nongbr_data_volume_ue, ul_nongbr_data_volume_ue=ul_nongbr_data_volume_ue)

Retrieve information on layer 2 measurements

Queries information about the layer 2 measurements.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RniApi()
app_ins_id = 'app_ins_id_example' # str | Application instance identifier (optional)
cell_id = ['cell_id_example'] # list[str] | Comma separated list of E-UTRAN Cell Identities (optional)
ue_ipv4_address = ['ue_ipv4_address_example'] # list[str] | Comma separated list of IE IPv4 addresses as defined for the type for AssociateId (optional)
ue_ipv6_address = ['ue_ipv6_address_example'] # list[str] | Comma separated list of IE IPv6 addresses as defined for the type for AssociateId (optional)
nated_ip_address = ['nated_ip_address_example'] # list[str] | Comma separated list of IE NATed IP addresses as defined for the type for AssociateId (optional)
gtp_teid = ['gtp_teid_example'] # list[str] | Comma separated list of GTP TEID addresses as defined for the type for AssociateId (optional)
dl_gbr_prb_usage_cell = 56 # int | PRB usage for downlink GBR traffic in percentage as defined in ETSI TS 136 314 (optional)
ul_gbr_prb_usage_cell = 56 # int | PRB usage for uplink GBR traffic in percentage as defined in ETSI TS 136 314 (optional)
dl_nongbr_prb_usage_cell = 56 # int | PRB usage for downlink non-GBR traffic in percentage as defined in ETSI TS 136 314 (optional)
ul_nongbr_prb_usage_cell = 56 # int | PRB usage for uplink non-GBR traffic in percentage as defined in ETSI TS 136 314 (optional)
dl_total_prb_usage_cell = 56 # int | PRB usage for total downlink traffic in percentage as defined in ETSI TS 136 314 (optional)
ul_total_prb_usage_cell = 56 # int | PRB usage for total uplink traffic in percentage as defined in ETSI TS 136 314 (optional)
received_dedicated_preambles_cell = 56 # int | Received dedicated preambles in percentage as defined in ETSI TS 136 314 (optional)
received_randomly_selected_preambles_low_range_cell = 56 # int | Received randomly selected preambles in the low range in percentage as defined in ETSI TS 136 314 (optional)
received_randomly_selected_preambles_high_range_cell = 56 # int | Received rendomly selected preambles in the high range in percentage as defined in ETSI TS 136 314 (optional)
number_of_active_ue_dl_gbr_cell = 56 # int | Number of active UEs with downlink GBR traffic as defined in ETSI TS 136 314 (optional)
number_of_active_ue_ul_gbr_cell = 56 # int | Number of active UEs with uplink GBR traffic as defined in ETSI TS 136 314 (optional)
number_of_active_ue_dl_nongbr_cell = 56 # int | Number of active UEs with downlink non-GBR traffic as defined in ETSI TS 136 314 (optional)
number_of_active_ue_ul_nongbr_cell = 56 # int | Number of active UEs with uplink non-GBR traffic as defined in ETSI TS 136 314 (optional)
dl_gbr_pdr_cell = 56 # int | Packet discard rate for downlink GBR traffic in percentage as defined in ETSI TS 136 314 (optional)
ul_gbr_pdr_cell = 56 # int | Packet discard rate for uplink GBR traffic in percentage as defined in ETSI TS 136 314 (optional)
dl_nongbr_pdr_cell = 56 # int | Packet discard rate for downlink non-GBR traffic in percentage as defined in ETSI TS 136 314 (optional)
ul_nongbr_pdr_cell = 56 # int | Packet discard rate for uplink non-GBR traffic in percentage as defined in ETSI TS 136 314 (optional)
dl_gbr_delay_ue = 56 # int | Packet delay of downlink GBR traffic of a UE as defined in ETSI TS 136 314 (optional)
ul_gbr_delay_ue = 56 # int | Packet delay of uplink GBR traffic of a UE as defined in ETSI TS 136 314 (optional)
dl_nongbr_delay_ue = 56 # int | Packet delay of downlink non-GBR traffic of a UE as defined in ETSI TS 136 314 (optional)
ul_nongbr_delay_ue = 56 # int | Packet delay of uplink non-GBR traffic of a UE as defined in ETSI TS 136 314 (optional)
dl_gbr_pdr_ue = 56 # int | Packet discard rate of downlink GBR traffic of a UE in percentage as defined in ETSI TS 136 314 (optional)
ul_gbr_pdr_ue = 56 # int | Packet discard rate of uplink GBR traffic of a UE in percentage as defined in ETSI TS 136 314 (optional)
dl_nongbr_pdr_ue = 56 # int | Packet discard rate of downlink non-GBR traffic of a UE in percentage as defined in ETSI TS 136 314 (optional)
ul_nongbr_pdr_ue = 56 # int | Packet discard rate of uplink non-GBR traffic of a UE in percentage as defined in ETSI TS 136 314 (optional)
dl_gbr_throughput_ue = 56 # int | Scheduled throughput of downlink GBR traffic of a UE as defined in ETSI TS 136 314 (optional)
ul_gbr_throughput_ue = 56 # int | Scheduled throughput of uplink GBR traffic of a UE as defined in ETSI TS 136 314 (optional)
dl_nongbr_throughput_ue = 56 # int | Scheduled throughput of downlink non-GBR traffic of a UE as defined in ETSI TS 136 314 (optional)
ul_nongbr_throughput_ue = 56 # int | Scheduled throughput of uplink non-GBR traffic of a UE as defined in ETSI TS 136 314 (optional)
dl_gbr_data_volume_ue = 56 # int | Data volume of downlink GBR traffic of a UE as defined in ETSI TS 136 314 (optional)
ul_gbr_data_volume_ue = 56 # int | Data volume of uplink GBR traffic of a UE as defined in ETSI TS 136 314 (optional)
dl_nongbr_data_volume_ue = 56 # int | Data volume of downlink non-GBR traffic of a UE as defined in ETSI TS 136 314 (optional)
ul_nongbr_data_volume_ue = 56 # int | Data volume of uplink non-GBR traffic of a UE as defined in ETSI TS 136 314 (optional)

try:
    # Retrieve information on layer 2 measurements
    api_response = api_instance.layer2_meas_info_get(app_ins_id=app_ins_id, cell_id=cell_id, ue_ipv4_address=ue_ipv4_address, ue_ipv6_address=ue_ipv6_address, nated_ip_address=nated_ip_address, gtp_teid=gtp_teid, dl_gbr_prb_usage_cell=dl_gbr_prb_usage_cell, ul_gbr_prb_usage_cell=ul_gbr_prb_usage_cell, dl_nongbr_prb_usage_cell=dl_nongbr_prb_usage_cell, ul_nongbr_prb_usage_cell=ul_nongbr_prb_usage_cell, dl_total_prb_usage_cell=dl_total_prb_usage_cell, ul_total_prb_usage_cell=ul_total_prb_usage_cell, received_dedicated_preambles_cell=received_dedicated_preambles_cell, received_randomly_selected_preambles_low_range_cell=received_randomly_selected_preambles_low_range_cell, received_randomly_selected_preambles_high_range_cell=received_randomly_selected_preambles_high_range_cell, number_of_active_ue_dl_gbr_cell=number_of_active_ue_dl_gbr_cell, number_of_active_ue_ul_gbr_cell=number_of_active_ue_ul_gbr_cell, number_of_active_ue_dl_nongbr_cell=number_of_active_ue_dl_nongbr_cell, number_of_active_ue_ul_nongbr_cell=number_of_active_ue_ul_nongbr_cell, dl_gbr_pdr_cell=dl_gbr_pdr_cell, ul_gbr_pdr_cell=ul_gbr_pdr_cell, dl_nongbr_pdr_cell=dl_nongbr_pdr_cell, ul_nongbr_pdr_cell=ul_nongbr_pdr_cell, dl_gbr_delay_ue=dl_gbr_delay_ue, ul_gbr_delay_ue=ul_gbr_delay_ue, dl_nongbr_delay_ue=dl_nongbr_delay_ue, ul_nongbr_delay_ue=ul_nongbr_delay_ue, dl_gbr_pdr_ue=dl_gbr_pdr_ue, ul_gbr_pdr_ue=ul_gbr_pdr_ue, dl_nongbr_pdr_ue=dl_nongbr_pdr_ue, ul_nongbr_pdr_ue=ul_nongbr_pdr_ue, dl_gbr_throughput_ue=dl_gbr_throughput_ue, ul_gbr_throughput_ue=ul_gbr_throughput_ue, dl_nongbr_throughput_ue=dl_nongbr_throughput_ue, ul_nongbr_throughput_ue=ul_nongbr_throughput_ue, dl_gbr_data_volume_ue=dl_gbr_data_volume_ue, ul_gbr_data_volume_ue=ul_gbr_data_volume_ue, dl_nongbr_data_volume_ue=dl_nongbr_data_volume_ue, ul_nongbr_data_volume_ue=ul_nongbr_data_volume_ue)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RniApi->layer2_meas_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_ins_id** | **str**| Application instance identifier | [optional] 
 **cell_id** | [**list[str]**](str.md)| Comma separated list of E-UTRAN Cell Identities | [optional] 
 **ue_ipv4_address** | [**list[str]**](str.md)| Comma separated list of IE IPv4 addresses as defined for the type for AssociateId | [optional] 
 **ue_ipv6_address** | [**list[str]**](str.md)| Comma separated list of IE IPv6 addresses as defined for the type for AssociateId | [optional] 
 **nated_ip_address** | [**list[str]**](str.md)| Comma separated list of IE NATed IP addresses as defined for the type for AssociateId | [optional] 
 **gtp_teid** | [**list[str]**](str.md)| Comma separated list of GTP TEID addresses as defined for the type for AssociateId | [optional] 
 **dl_gbr_prb_usage_cell** | **int**| PRB usage for downlink GBR traffic in percentage as defined in ETSI TS 136 314 | [optional] 
 **ul_gbr_prb_usage_cell** | **int**| PRB usage for uplink GBR traffic in percentage as defined in ETSI TS 136 314 | [optional] 
 **dl_nongbr_prb_usage_cell** | **int**| PRB usage for downlink non-GBR traffic in percentage as defined in ETSI TS 136 314 | [optional] 
 **ul_nongbr_prb_usage_cell** | **int**| PRB usage for uplink non-GBR traffic in percentage as defined in ETSI TS 136 314 | [optional] 
 **dl_total_prb_usage_cell** | **int**| PRB usage for total downlink traffic in percentage as defined in ETSI TS 136 314 | [optional] 
 **ul_total_prb_usage_cell** | **int**| PRB usage for total uplink traffic in percentage as defined in ETSI TS 136 314 | [optional] 
 **received_dedicated_preambles_cell** | **int**| Received dedicated preambles in percentage as defined in ETSI TS 136 314 | [optional] 
 **received_randomly_selected_preambles_low_range_cell** | **int**| Received randomly selected preambles in the low range in percentage as defined in ETSI TS 136 314 | [optional] 
 **received_randomly_selected_preambles_high_range_cell** | **int**| Received rendomly selected preambles in the high range in percentage as defined in ETSI TS 136 314 | [optional] 
 **number_of_active_ue_dl_gbr_cell** | **int**| Number of active UEs with downlink GBR traffic as defined in ETSI TS 136 314 | [optional] 
 **number_of_active_ue_ul_gbr_cell** | **int**| Number of active UEs with uplink GBR traffic as defined in ETSI TS 136 314 | [optional] 
 **number_of_active_ue_dl_nongbr_cell** | **int**| Number of active UEs with downlink non-GBR traffic as defined in ETSI TS 136 314 | [optional] 
 **number_of_active_ue_ul_nongbr_cell** | **int**| Number of active UEs with uplink non-GBR traffic as defined in ETSI TS 136 314 | [optional] 
 **dl_gbr_pdr_cell** | **int**| Packet discard rate for downlink GBR traffic in percentage as defined in ETSI TS 136 314 | [optional] 
 **ul_gbr_pdr_cell** | **int**| Packet discard rate for uplink GBR traffic in percentage as defined in ETSI TS 136 314 | [optional] 
 **dl_nongbr_pdr_cell** | **int**| Packet discard rate for downlink non-GBR traffic in percentage as defined in ETSI TS 136 314 | [optional] 
 **ul_nongbr_pdr_cell** | **int**| Packet discard rate for uplink non-GBR traffic in percentage as defined in ETSI TS 136 314 | [optional] 
 **dl_gbr_delay_ue** | **int**| Packet delay of downlink GBR traffic of a UE as defined in ETSI TS 136 314 | [optional] 
 **ul_gbr_delay_ue** | **int**| Packet delay of uplink GBR traffic of a UE as defined in ETSI TS 136 314 | [optional] 
 **dl_nongbr_delay_ue** | **int**| Packet delay of downlink non-GBR traffic of a UE as defined in ETSI TS 136 314 | [optional] 
 **ul_nongbr_delay_ue** | **int**| Packet delay of uplink non-GBR traffic of a UE as defined in ETSI TS 136 314 | [optional] 
 **dl_gbr_pdr_ue** | **int**| Packet discard rate of downlink GBR traffic of a UE in percentage as defined in ETSI TS 136 314 | [optional] 
 **ul_gbr_pdr_ue** | **int**| Packet discard rate of uplink GBR traffic of a UE in percentage as defined in ETSI TS 136 314 | [optional] 
 **dl_nongbr_pdr_ue** | **int**| Packet discard rate of downlink non-GBR traffic of a UE in percentage as defined in ETSI TS 136 314 | [optional] 
 **ul_nongbr_pdr_ue** | **int**| Packet discard rate of uplink non-GBR traffic of a UE in percentage as defined in ETSI TS 136 314 | [optional] 
 **dl_gbr_throughput_ue** | **int**| Scheduled throughput of downlink GBR traffic of a UE as defined in ETSI TS 136 314 | [optional] 
 **ul_gbr_throughput_ue** | **int**| Scheduled throughput of uplink GBR traffic of a UE as defined in ETSI TS 136 314 | [optional] 
 **dl_nongbr_throughput_ue** | **int**| Scheduled throughput of downlink non-GBR traffic of a UE as defined in ETSI TS 136 314 | [optional] 
 **ul_nongbr_throughput_ue** | **int**| Scheduled throughput of uplink non-GBR traffic of a UE as defined in ETSI TS 136 314 | [optional] 
 **dl_gbr_data_volume_ue** | **int**| Data volume of downlink GBR traffic of a UE as defined in ETSI TS 136 314 | [optional] 
 **ul_gbr_data_volume_ue** | **int**| Data volume of uplink GBR traffic of a UE as defined in ETSI TS 136 314 | [optional] 
 **dl_nongbr_data_volume_ue** | **int**| Data volume of downlink non-GBR traffic of a UE as defined in ETSI TS 136 314 | [optional] 
 **ul_nongbr_data_volume_ue** | **int**| Data volume of uplink non-GBR traffic of a UE as defined in ETSI TS 136 314 | [optional] 

### Return type

[**L2Meas**](L2Meas.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plmn_info_get**
> list[PlmnInfo] plmn_info_get(app_ins_id)

Retrieve information on the underlying Mobile Network that the MEC application is associated to

Queries information about the Mobile Network

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RniApi()
app_ins_id = ['app_ins_id_example'] # list[str] | Comma separated list of Application instance identifiers

try:
    # Retrieve information on the underlying Mobile Network that the MEC application is associated to
    api_response = api_instance.plmn_info_get(app_ins_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RniApi->plmn_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_ins_id** | [**list[str]**](str.md)| Comma separated list of Application instance identifiers | 

### Return type

[**list[PlmnInfo]**](PlmnInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rab_info_get**
> RabInfo rab_info_get(app_ins_id=app_ins_id, cell_id=cell_id, ue_ipv4_address=ue_ipv4_address, ue_ipv6_address=ue_ipv6_address, nated_ip_address=nated_ip_address, gtp_teid=gtp_teid, erab_id=erab_id, qci=qci, erab_mbr_dl=erab_mbr_dl, erab_mbr_ul=erab_mbr_ul, erab_gbr_dl=erab_gbr_dl, erab_gbr_ul=erab_gbr_ul)

Retrieve information on Radio Access Bearers

Queries information about the Radio Access Bearers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RniApi()
app_ins_id = 'app_ins_id_example' # str | Application instance identifier (optional)
cell_id = ['cell_id_example'] # list[str] | Comma separated list of E-UTRAN Cell Identities (optional)
ue_ipv4_address = ['ue_ipv4_address_example'] # list[str] | Comma separated list of IE IPv4 addresses as defined for the type for AssociateId (optional)
ue_ipv6_address = ['ue_ipv6_address_example'] # list[str] | Comma separated list of IE IPv6 addresses as defined for the type for AssociateId (optional)
nated_ip_address = ['nated_ip_address_example'] # list[str] | Comma separated list of IE NATed IP addresses as defined for the type for AssociateId (optional)
gtp_teid = ['gtp_teid_example'] # list[str] | Comma separated list of GTP TEID addresses as defined for the type for AssociateId (optional)
erab_id = 56 # int | E-RAB identifier (optional)
qci = 56 # int | QoS Class Identifier as defined in ETSI TS 123 401 (optional)
erab_mbr_dl = 56 # int | Maximum downlink E-RAB Bit Rate as defined in ETSI TS 123 401 (optional)
erab_mbr_ul = 56 # int | Maximum uplink E-RAB Bit Rate as defined in ETSI TS 123 401 (optional)
erab_gbr_dl = 56 # int | Guaranteed downlink E-RAB Bit Rate as defined in ETSI TS 123 401 (optional)
erab_gbr_ul = 56 # int | Guaranteed uplink E-RAB Bit Rate as defined in ETSI TS 123 401 (optional)

try:
    # Retrieve information on Radio Access Bearers
    api_response = api_instance.rab_info_get(app_ins_id=app_ins_id, cell_id=cell_id, ue_ipv4_address=ue_ipv4_address, ue_ipv6_address=ue_ipv6_address, nated_ip_address=nated_ip_address, gtp_teid=gtp_teid, erab_id=erab_id, qci=qci, erab_mbr_dl=erab_mbr_dl, erab_mbr_ul=erab_mbr_ul, erab_gbr_dl=erab_gbr_dl, erab_gbr_ul=erab_gbr_ul)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RniApi->rab_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_ins_id** | **str**| Application instance identifier | [optional] 
 **cell_id** | [**list[str]**](str.md)| Comma separated list of E-UTRAN Cell Identities | [optional] 
 **ue_ipv4_address** | [**list[str]**](str.md)| Comma separated list of IE IPv4 addresses as defined for the type for AssociateId | [optional] 
 **ue_ipv6_address** | [**list[str]**](str.md)| Comma separated list of IE IPv6 addresses as defined for the type for AssociateId | [optional] 
 **nated_ip_address** | [**list[str]**](str.md)| Comma separated list of IE NATed IP addresses as defined for the type for AssociateId | [optional] 
 **gtp_teid** | [**list[str]**](str.md)| Comma separated list of GTP TEID addresses as defined for the type for AssociateId | [optional] 
 **erab_id** | **int**| E-RAB identifier | [optional] 
 **qci** | **int**| QoS Class Identifier as defined in ETSI TS 123 401 | [optional] 
 **erab_mbr_dl** | **int**| Maximum downlink E-RAB Bit Rate as defined in ETSI TS 123 401 | [optional] 
 **erab_mbr_ul** | **int**| Maximum uplink E-RAB Bit Rate as defined in ETSI TS 123 401 | [optional] 
 **erab_gbr_dl** | **int**| Guaranteed downlink E-RAB Bit Rate as defined in ETSI TS 123 401 | [optional] 
 **erab_gbr_ul** | **int**| Guaranteed uplink E-RAB Bit Rate as defined in ETSI TS 123 401 | [optional] 

### Return type

[**RabInfo**](RabInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s1_bearer_info_get**
> S1BearerInfo s1_bearer_info_get(temp_ue_id=temp_ue_id, ue_ipv4_address=ue_ipv4_address, ue_ipv6_address=ue_ipv6_address, nated_ip_address=nated_ip_address, gtp_teid=gtp_teid, cell_id=cell_id, erab_id=erab_id)

Retrieve S1-U bearer information related to specific UE(s)

Queries information about the S1 bearer(s)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RniApi()
temp_ue_id = ['temp_ue_id_example'] # list[str] | Comma separated list of temporary identifiers allocated for the specific UE as defined in   ETSI TS 136 413 (optional)
ue_ipv4_address = ['ue_ipv4_address_example'] # list[str] | Comma separated list of IE IPv4 addresses as defined for the type for AssociateId (optional)
ue_ipv6_address = ['ue_ipv6_address_example'] # list[str] | Comma separated list of IE IPv6 addresses as defined for the type for AssociateId (optional)
nated_ip_address = ['nated_ip_address_example'] # list[str] | Comma separated list of IE NATed IP addresses as defined for the type for AssociateId (optional)
gtp_teid = ['gtp_teid_example'] # list[str] | Comma separated list of GTP TEID addresses as defined for the type for AssociateId (optional)
cell_id = ['cell_id_example'] # list[str] | Comma separated list of E-UTRAN Cell Identities (optional)
erab_id = [56] # list[int] | Comma separated list of E-RAB identifiers (optional)

try:
    # Retrieve S1-U bearer information related to specific UE(s)
    api_response = api_instance.s1_bearer_info_get(temp_ue_id=temp_ue_id, ue_ipv4_address=ue_ipv4_address, ue_ipv6_address=ue_ipv6_address, nated_ip_address=nated_ip_address, gtp_teid=gtp_teid, cell_id=cell_id, erab_id=erab_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RniApi->s1_bearer_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **temp_ue_id** | [**list[str]**](str.md)| Comma separated list of temporary identifiers allocated for the specific UE as defined in   ETSI TS 136 413 | [optional] 
 **ue_ipv4_address** | [**list[str]**](str.md)| Comma separated list of IE IPv4 addresses as defined for the type for AssociateId | [optional] 
 **ue_ipv6_address** | [**list[str]**](str.md)| Comma separated list of IE IPv6 addresses as defined for the type for AssociateId | [optional] 
 **nated_ip_address** | [**list[str]**](str.md)| Comma separated list of IE NATed IP addresses as defined for the type for AssociateId | [optional] 
 **gtp_teid** | [**list[str]**](str.md)| Comma separated list of GTP TEID addresses as defined for the type for AssociateId | [optional] 
 **cell_id** | [**list[str]**](str.md)| Comma separated list of E-UTRAN Cell Identities | [optional] 
 **erab_id** | [**list[int]**](int.md)| Comma separated list of E-RAB identifiers | [optional] 

### Return type

[**S1BearerInfo**](S1BearerInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_link_list_subscriptions_get**
> SubscriptionLinkList subscription_link_list_subscriptions_get(subscription_type=subscription_type)

Retrieve information on subscriptions for notifications

Queries information on subscriptions for notifications

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RniApi()
subscription_type = 'subscription_type_example' # str | Filter on a specific subscription type. Permitted values: cell_change, rab_est, rab_mod, rab_rel, meas_rep_ue, nr_meas_rep_ue, timing_advance_ue, ca_reconf, s1_bearer. (optional)

try:
    # Retrieve information on subscriptions for notifications
    api_response = api_instance.subscription_link_list_subscriptions_get(subscription_type=subscription_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RniApi->subscription_link_list_subscriptions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_type** | **str**| Filter on a specific subscription type. Permitted values: cell_change, rab_est, rab_mod, rab_rel, meas_rep_ue, nr_meas_rep_ue, timing_advance_ue, ca_reconf, s1_bearer. | [optional] 

### Return type

[**SubscriptionLinkList**](SubscriptionLinkList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_delete**
> subscriptions_delete(subscription_id)

Cancel an existing subscription

Cancels an existing subscription, identified by its self-referring URI returned on creation (initial POST)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RniApi()
subscription_id = 'subscription_id_example' # str | Subscription Id, specifically the \"Self-referring URI\" returned in the subscription request

try:
    # Cancel an existing subscription
    api_instance.subscriptions_delete(subscription_id)
except ApiException as e:
    print("Exception when calling RniApi->subscriptions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription Id, specifically the \&quot;Self-referring URI\&quot; returned in the subscription request | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_get**
> InlineSubscription subscriptions_get(subscription_id)

Retrieve information on current specific subscription

Queries information about an existing subscription, identified by its self-referring URI returned on creation (initial POST)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RniApi()
subscription_id = 'subscription_id_example' # str | Subscription Id, specifically the \"Self-referring URI\" returned in the subscription request

try:
    # Retrieve information on current specific subscription
    api_response = api_instance.subscriptions_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RniApi->subscriptions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription Id, specifically the \&quot;Self-referring URI\&quot; returned in the subscription request | 

### Return type

[**InlineSubscription**](InlineSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_post**
> InlineSubscription subscriptions_post(body)

Create a new subscription

Creates a new subscription to Radio Network Information notifications

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RniApi()
body = swagger_client.InlineSubscription() # InlineSubscription | Subscription to be created

try:
    # Create a new subscription
    api_response = api_instance.subscriptions_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RniApi->subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineSubscription**](InlineSubscription.md)| Subscription to be created | 

### Return type

[**InlineSubscription**](InlineSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_put**
> InlineSubscription subscriptions_put(body, subscription_id)

Modify an existing subscription

Updates an existing subscription, identified by its self-referring URI returned on creation (initial POST)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RniApi()
body = swagger_client.InlineSubscription() # InlineSubscription | Subscription to be modified
subscription_id = 'subscription_id_example' # str | Subscription Id, specifically the \"Self-referring URI\" returned in the subscription request

try:
    # Modify an existing subscription
    api_response = api_instance.subscriptions_put(body, subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RniApi->subscriptions_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineSubscription**](InlineSubscription.md)| Subscription to be modified | 
 **subscription_id** | **str**| Subscription Id, specifically the \&quot;Self-referring URI\&quot; returned in the subscription request | 

### Return type

[**InlineSubscription**](InlineSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


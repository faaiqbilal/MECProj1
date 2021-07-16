from __future__ import print_function
import time
import swagger_client
from swagger_client.configuration import Configuration
import json
from swagger_client.rest import ApiException
from pprint import pprint


configuration = Configuration()
configuration.host = "https://try-mec.etsi.org/sbxq2fy6x5/rni/v2"

# create an instance of the API class
api_instance = swagger_client.RniApi(swagger_client.ApiClient(configuration))
app_ins_id = ['10.10.0.1', '10.100.0.1'] # list[str] | Comma separated list of Application instance identifiers

try:
    api_response = api_instance.rab_info_get()
    pprint(api_response.cell_user_info)
except ApiException as e:
    print("Exception when calling RniApi->rab_info_get: %s\n" % e)
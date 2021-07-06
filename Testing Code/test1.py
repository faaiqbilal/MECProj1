from __future__ import print_function
import time
import swagger_client
from swagger_client.configuration import Configuration
from swagger_client.rest import ApiException
from pprint import pprint


configuration = Configuration()
configuration.host = "https://try-mec.etsi.org/sbxyljdrf7/rni/v2"

# create an instance of the API class
api_instance = swagger_client.RniApi(swagger_client.ApiClient(configuration))
app_ins_id = ['10.10.0.1', '10.100.0.1'] # list[str] | Comma separated list of Application instance identifiers

try:
    # Retrieve information on the underlying Mobile Network that the MEC application is associated to
    api_response = api_instance.plmn_info_get(app_ins_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RniApi->plmn_info_get: %s\n" % e)


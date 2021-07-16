from __future__ import print_function
import time
import swagger_client
from swagger_client.configuration import Configuration
from swagger_client.rest import ApiException
from pprint import pprint

configuration = Configuration()
configuration.host = "https://try-mec.etsi.org/sbxa33vybk/rni/v2"

api_instance = swagger_client.RniApi(swagger_client.ApiClient(configuration))

app_ins_id = ['10.10.0.1', '10.100.0.1'] # list[str] | Comma separated list of Application instance identifiers



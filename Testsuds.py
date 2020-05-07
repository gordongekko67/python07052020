from suds.client import Client
url_service = 'http://www.onvif.org/ver10/device/wsdl'
#url_service = 'https://www.onvif.org/ver10/device/wsdl/devicemgmt.wsdl'

client = Client(url_service)
list_of_methods = [method for method in client.wsdl.services[0].ports[0].methods]

print (list_of_methods)

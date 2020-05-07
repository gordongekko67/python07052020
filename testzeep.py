import zeep
import  lxml

wsdl =  'https://www.onvif.org/ver10/events/wsdl/event.wsdl'

client = Client(wsdl)

print(client.namespaces)

list_of_methods = [method for method in client.wsdl.services[0].ports[0].methods]
list_of_services = [method for method in client.wsdl.messages[0].ports[0].methods]
list_of_services1 = [method for method in client.wsdl.types[0].ports[0].methods]

order_type = client.get_type('ns0:Order')

print (list_of_methods)
print (list_of_services)
print (list_of_services1)
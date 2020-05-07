import suds
from suds.client import Client;

url =  'https://www.onvif.org/ver10/device/wsdl/devicemgmt.wsdl'

def list_all(url):
    client = suds.client.Client(url)
    print(client)
    for service in client.wsdl.services:
        for port in service.ports:
            methods = port.methods.values()
            for method in methods:
                print(method.name)
                for part in method.soap.input.body.parts:
                    part_type = part.type
                    if (not part_type):
                        part_type = part.element[0]
                    print('  ' + str(part.name) + ': ' + str(part_type))
                    o = client.factory.create(part_type)
                    print('    ' + str(o))




list_all(url)





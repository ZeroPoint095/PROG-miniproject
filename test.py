print('Nein')

api_url = 'http://webservices.ns.nl/ns-api-storingen?station=ut'
response = requests.get(api_url, auth=auth_details)

storingenXML = xmltodict.parse(response.text)

print('Dit zijn de treinen met een storing: ')
for storing in storingenXML[]

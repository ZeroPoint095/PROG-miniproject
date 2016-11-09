import requests
import xmltodict

email = 'email'
wachtwoord = 'ww'

auth_details = (email, wachtwoord)
api_url = 'https://webservices.ns.nl/ns-api-avt?station=ut'
response = requests.get(api_url, auth=auth_details)

vertrekkenXML = xmltodict.parse(response.text)

print('Dit zijn de vertrekkende treinen')
for vertrek in vertrekkenXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    vertraging = []
    route = []
    eindbestemming = vertrek['EindBestemming']

    vertrektijd = vertrek['VertrekTijd']
    vertrektijd = vertrektijd[11:16]
    treintype = vertrek['TreinSoort']
    spoor = vertrek['VertrekSpoor']['#text']
    if 'VertrekVertraging' in vertrek:
                VertrekVertragingTekst = vertrek['VertrekVertragingTekst']
                vertraging = VertrekVertragingTekst
    else:
        vertraging = 'geen vertraging'
    if 'RouteTekst' in vertrek:
                route = vertrek['RouteTekst']
    else:
        route = 'geen tussenstations'

    print('Om ' + vertrektijd + ' vertrekt een trein (' + treintype+  ') naar ' + eindbestemming + ' van spoor ' + spoor + ' met een eventuele vertraging van: ' + vertraging + '.'
          + ' De eventuele tussenstations zijn: ' + route)

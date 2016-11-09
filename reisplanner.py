import requests
import xmltodict
from API_NS import (auth_details)
import time

huidigeStation='Utrecht+Centraal'
bestemming='Woerden'

api_url = 'http://webservices.ns.nl/ns-api-treinplanner?fromStation='+huidigeStation+'&toStation='+bestemming+'&departure=trueexterne'
response = requests.get(api_url, auth=auth_details)

reisplannerXML = xmltodict.parse(response.text)

def optimaalReis():
    for xml in reisplannerXML['ReisMogelijkheden']['ReisMogelijkheid']:
        if xml['Optimaal'] == 'true':
            tijd=xml['ActueleVertrekTijd']
            tijd=tijd[11:16]
            spoor=xml['ReisDeel']['ReisStop'][0]['Spoor']['#text']
            trein=xml['ReisDeel']['VervoerType']
            print('De eerst de beste mogelijkheid is de',trein,'om',tijd,'vanaf spoor', spoor)
# optimaal = reisplannerXML['ReisMogelijkheden']['ReisMogelijkheid']['Optimaal']
# actueleVertrektijd = reisplannerXML['ReisMogelijkheden']['ReisMogelijkheid']['ActueleVertrekTijd']
# vertrekSpoor = reisplannerXML['ReisMogelijkheden']['ReisMogelijkheid']['ReisDeel']['Reisstop']['Spoor']
# overstap = reisplannerXML['ReisMogelijkheden']['ReisMogelijkheid']

optimaalReis()

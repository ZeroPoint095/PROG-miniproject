import requests
import xmltodict
from API_NS import (auth_details)
import time

huidigeStation='Utrecht Centraal'
bestemming='Woerden'

api_url = 'http://webservices.ns.nl/ns-api-treinplanner?fromStation='+huidigeStation+'&toStation='+bestemming+'&departure=trueexterne'
response = requests.get(api_url, auth=auth_details)

reisplannerXML = xmltodict.parse(response.text)

def optimaalReis():
    'Returnt de eerste de beste vertrektijd, spoor nummer en treinsoort'
    for xml in reisplannerXML['ReisMogelijkheden']['ReisMogelijkheid']:
        if xml['Optimaal'] == 'true':
            tijd=xml['ActueleVertrekTijd']
            tijd=tijd[11:16]
            spoor=xml['ReisDeel']['ReisStop'][0]['Spoor']['#text']
            trein=xml['ReisDeel']['VervoerType']
    return tijd, spoor, trein
### mislukte xml parse pogingen ###
# optimaal = reisplannerXML['ReisMogelijkheden']['ReisMogelijkheid']['Optimaal']
# actueleVertrektijd = reisplannerXML['ReisMogelijkheden']['ReisMogelijkheid']['ActueleVertrekTijd']
# vertrekSpoor = reisplannerXML['ReisMogelijkheden']['ReisMogelijkheid']['ReisDeel']['Reisstop']['Spoor']
# overstap = reisplannerXML['ReisMogelijkheden']['ReisMogelijkheid']

def printTest():
    'laat zien de verschillende print mogelijkheden'
    #resultaat als lijst
    print(optimaalReis())
    #resultaat als 3 losse strings
    print(optimaalReis()[0], optimaalReis()[1], optimaalReis()[2])
    #resultaat in een zin
    print('De eerste de beste',optimaalReis()[2],'trein vertrekt om',optimaalReis()[0],'vanaf spoor',optimaalReis()[1])

printTest()

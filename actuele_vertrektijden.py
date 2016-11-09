import requests
import xmltodict
from API_NS import (auth_details, api_url)

response = requests.get(api_url, auth=auth_details)
vertrekkenXML = xmltodict.parse(response.text)

def actuele_vertrekinformatie():
    uitvoer=['Dit zijn de vertrekkende treinen het komende uur']
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

        uitvoer_avt = 'Om '+vertrektijd + ' vertrekt een trein (' + treintype+  ') naar ' + eindbestemming + ' van spoor ' + spoor + ' met een eventuele vertraging van: ' + vertraging + '.' + '\n '+  ' De eventuele tussenstations zijn: ' + route
        uitvoer += [uitvoer_avt]
    return uitvoer
actuele_vertrekinformatie()

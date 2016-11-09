import requests
import xmltodict
from API_NS import (auth_details, api_url)

response = requests.get(api_url, auth=auth_details)
storingXML = xmltodict.parse(response.text)

vertrekkenXML = xmltodict.parse(response.text)
def actuele_vertrekinformatie():
    print('Dit zijn de vertrekkende treinen het komende uur')
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
              + '\n '+  ' De eventuele tussenstations zijn: ' + route)
actuele_vertrekinformatie()

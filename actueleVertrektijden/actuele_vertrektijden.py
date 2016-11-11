import requests
import xmltodict
from API_NS import (auth_details, api_url)  ##API instellingen importeren

##API gegevens en XML verwerken##
response = requests.get(api_url, auth=auth_details)
vertrekkenXML = xmltodict.parse(response.text)

##Functie voor het verwerken van de informatie uit de XML
def actuele_vertrekinformatie():
    uitvoer_avt_final=['Dit zijn de vertrekkende treinen het komende uur']
    for vertrek in vertrekkenXML['ActueleVertrekTijden']['VertrekkendeTrein']:  ##Loopt door het XML bestand
        vertraging = []
        route = []
        eindbestemming = vertrek['EindBestemming']  ##Haalt de eindbestemming op

        vertrektijd = vertrek['VertrekTijd']    ##Haalt de vertrektijd op
        vertrektijd = vertrektijd[11:16]        ##Veranderd de notatie van de tijd
        treintype = vertrek['TreinSoort']       ##Haalt het treintype op
        spoor = vertrek['VertrekSpoor']['#text']    ##Haalt het vertrekspoor
        if 'VertrekVertraging' in vertrek:      ##Kijkt of er vertraging is
                    VertrekVertragingTekst = vertrek['VertrekVertragingTekst']
                    vertraging = VertrekVertragingTekst
        else:
            vertraging = '+0'
        if 'RouteTekst' in vertrek:     ##Kijkt of er tussenstations zijn op het traject
                    route = vertrek['RouteTekst']
        else:
            route = 'geen tussenstations'
        ##Uitvoer van alle opties
        #uitvoer_avt = 'Om '+vertrektijd + ' vertrekt een trein (' + treintype+  ') naar ' + eindbestemming + ' van spoor ' + spoor + ' met een eventuele vertraging van: ' + vertraging + '.' + '\n '+  ' De eventuele tussenstations zijn: ' + route
        uitvoer_avt = '\n ' + vertrektijd + vertraging + ' naar '+ eindbestemming + ' ' + 'Spoor: ' + spoor
        ##Uitvoer wordt toegevoegd aan een lijst
        uitvoer_avt_final += [uitvoer_avt]
    return uitvoer_avt_final        ##Returned de complete uitvoer in een lijst

print(actuele_vertrekinformatie())

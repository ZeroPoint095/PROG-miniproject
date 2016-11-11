from collections import defaultdict

import requests
import xmltodict
from API_NS import (auth_details, api_url_storingen)
import re

#Hier wordt het XML-bestand aangeroepen uit het bestand API_NS.py
response = requests.get(api_url_storingen, auth=auth_details)
storingXML = xmltodict.parse(response.text, dict_constructor=lambda *args, **kwargs: defaultdict(list, *args, **kwargs))

def storingen_ophalen_gepland():                                               #Hier begint de Functie die geplande storingen ophaalt

    uitvoerSTR = []                                                            #Uitvoer is een lege list
    try:
        for storing in storingXML['Storingen'][0]['Gepland'][0]['Storing']:    #Loopt door de xml file
            traject = storing['Traject'][0]                                    #Haalt uit de key storing de tag Traject
            bericht = storing['Bericht'][0]                                    #Haalt uit de key storing de tag Bericht
            bericht_new = re.sub("<.*?>", "", bericht)                         #Maakt van de variabele Bericht, een nieuwe variabele zonder de Html-tags
            storingen_uitvoer = 'Traject:' + traject + bericht_new             #Voegt Traject en het bericht samen tot een bericht
            uitvoerSTR += [storingen_uitvoer]                                  #Hierin worden de berichten samen met het traject toegevoegt aan een list
    except:
        uitvoerSTR = ['Er zijn geen geplande storingen\n']                     #Als er geen keys traject en bericht voorkomen, wordt er een foutmelding laten zien
    return uitvoerSTR

print(storingen_ophalen_gepland())

def storingen_ophalen_ongepland():                                             #Hier begint de Functie die ongeplande storingen ophaalt

    uitvoerSTR = []                                                            #Uitvoer is een lege list
    try:
       for storing in storingXML['Storingen'][0]['Ongepland'][0]['Storing']:      #Loopt door de xml file
            traject = storing['Traject'][0]                                    #Haalt uit de key storing de tag Traject
            bericht = storing['Bericht'][0]                                    #Haalt uit de key storing de tag Bericht
            bericht_new = re.sub("<.*?>", "", bericht)                      #Maakt van de variabele Bericht, een nieuwe variabele zonder de Html-tags
            storingen_uitvoer = 'Traject:' + traject + bericht_new          #Voegt Traject en het bericht samen tot een bericht
            uitvoerSTR += [storingen_uitvoer]                               #Hierin worden de berichten samen met het traject toegevoegt aan een list
    except:
        uitvoerSTR = ['Er zijn geen ongeplande storingen']                  #Als er geen keys traject en bericht voorkomen, wordt er een foutmelding laten zien

    return uitvoerSTR

print(storingen_ophalen_ongepland())

import requests
import xmltodict
from API_NS import (auth_details, api_url_storingen)
import re
#Hier wordt het XML-bestand aangeroepen uit het bestand API_NS.py
response = requests.get(api_url_storingen, auth=auth_details)
storingXML = xmltodict.parse(response.text)

#Hier begint de Functie die alle storingen ophaalt
def storingen_ophalen():

    #Uitvoer is een lege list
    uitvoerSTR = []
    try:
        for storing in storingXML['Storingen']['Gepland']['Storing']:       #Loopt door de xml file
            traject = storing['Traject']                                    #Haalt uit de key storing de tag Traject
            bericht = storing['Bericht']                                    #Haalt uit de key storing de tag Bericht
            bericht_new = re.sub("<.*?>", "", bericht)                      #Maakt van de variabele Bericht, een nieuwe variabele zonder de Html-tags
            storingen_uitvoer = 'Traject:' + traject + bericht_new          #Voegt Traject en het bericht samen tot een bericht
            uitvoerSTR += [storingen_uitvoer]                               #Hierin worden de berichten samen met het traject toegevoegt aan een list
    except:
        uitvoerSTR = ['Er zijn geen storingen']                             #Als er geen keys traject en bericht voorkomen, wordt er een foutmelding laten zien

    return uitvoerSTR


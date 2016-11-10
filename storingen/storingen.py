import requests
import xmltodict
from API_NS import (auth_details, api_url_storingen)
import re

response = requests.get(api_url_storingen, auth=auth_details)
storingXML = xmltodict.parse(response.text)

def storingen_ophalen():

    uitvoerSTR = []
    try:
        for storing in storingXML['Storingen']['Gepland']['Storing']:
            traject = storing['Traject']
            bericht = storing['Bericht']
            bericht_new = re.sub("<.*?>", "", bericht)
            storingen_uitvoer = 'Traject:' + traject + bericht_new
            uitvoerSTR += [storingen_uitvoer]
        for item in uitvoerSTR:
            print(item)
    except:
        uitvoerSTR = ['Er zijn geen storingen']

    return uitvoerSTR


import requests
import xmltodict
from API_NS import (auth_details, api_url_storingen)
import html

response = requests.get(api_url_storingen, auth=auth_details)
storingXML = xmltodict.parse(response.text)

def gepland():
    for storing in storingXML['Storingen']['Gepland']['Storing']:
        traject = storing['Traject']
        periode = storing['Periode']
        bericht = storing['Bericht']
        print(bericht)

gepland()

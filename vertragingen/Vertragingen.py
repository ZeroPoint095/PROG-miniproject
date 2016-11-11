#code samengesteld door Roel meijer

import requests
import xmltodict

from API_NS import (auth_details,
                     api_url)

# with open('offlinevert.xml') as myXMLfile:
#      dienstRegelingXML = xmltodict.parse(myXMLfile.read(),dict_constructor=dict)

def vertragingen():
    Uitvoer_vertragingen = []
    #For-loop die XML data controleerd op vertragingen.
    for treinRit in dienstRegelingXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        #print('VertrekVertragingTekst' in treinRit)
        #print(treinRit)
        #Als er vertragingen zijn wordt deze IF-statement uitgevoerd.
        if 'VertrekVertragingTekst' in treinRit:

            #If en else statements voor het geval trajecten geen tussenstations hebben.
            if 'RouteTekst' in treinRit:
                TussenStations = ' met tussenstation(s) ' + treinRit['RouteTekst']

            else:
                TussenStations = ''

            VertrekTijd = treinRit['VertrekTijd']
            VertrekTijd = VertrekTijd[11:16]
            Vertraging = treinRit['VertrekVertragingTekst']
            EindBestemming = treinRit['EindBestemming']
            TreinSoort = treinRit['TreinSoort']
            #Voegt alle vertragingen toe aan uitvoerlijst.
            Uitvoer_vertragingen += ['De ' + color.BOLD + TreinSoort + color.END + ' naar ' + color.BOLD + EindBestemming + TussenStations + color.END + ' van ' + color.BOLD + VertrekTijd + color.END + ' heeft een vertraging van ' + color.BOLD + Vertraging + color.END + '.']

    #Als er geen vertragingen aan de uitvoerlijst zijn toegevoegd wordt dit aan de lijst toegevoegd.
    if len(Uitvoer_vertragingen) == 0:
        Uitvoer_vertragingen = ['Er zijn op dit moment geen vertragingen bekend.']

    print(Uitvoer_vertragingen)
    #Uitvoerlijst versturen naar hoofdprogramma.
    return Uitvoer_vertragingen

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

response = requests.get(api_url, auth=auth_details)
dienstRegelingXML = xmltodict.parse(response.text)
vertragingen()


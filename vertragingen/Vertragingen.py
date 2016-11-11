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
            Uitvoer_vertragingen += ['De ' + TreinSoort + ' naar ' + EindBestemming + TussenStations + ' van ' + VertrekTijd + ' heeft een vertraging van ' + Vertraging + '.']

    #Als er geen vertragingen aan de uitvoerlijst zijn toegevoegd wordt dit aan de lijst toegevoegd.
    if len(Uitvoer_vertragingen) == 0:
        Uitvoer_vertragingen = ['Er zijn op dit moment geen vertragingen bekend.']

    print(Uitvoer_vertragingen)
    #Uitvoerlijst versturen naar hoofdprogramma.
    return Uitvoer_vertragingen

response = requests.get(api_url, auth=auth_details)
dienstRegelingXML = xmltodict.parse(response.text)
vertragingen()


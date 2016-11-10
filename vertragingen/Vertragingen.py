#code samengesteld door Roel meijer

import requests
import xmltodict

from API_NS import (auth_details,
                    api_url)

def vertragingen():
    Uitvoer_vertragingen = []
    #for-loop die XML data controleerd op vertragingen.
    for treinRitten in dienstRegelingXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        print('VertrekVertragingTekst' in treinRitten)
        print(treinRitten)

        if 'VertrekVertragingTekst' in treinRitten:

            #If en else statements voor het geval trajecten geen tussenstations hebben.
            if 'RouteTekst' in treinRitten:
                TussenStations = treinRitten['RouteTekst'] + ' met als eindbestemming '

            else:
                TussenStations = ''

            VertrekTijd = treinRitten['VertrekTijd']
            VertrekTijd = VertrekTijd[11:16]
            Vertraging = treinRitten['VertrekVertragingTekst']
            EindBestemming = treinRitten['EindBestemming']
            TreinSoort = treinRitten['TreinSoort']

            Uitvoer_vertragingen += ['De ' + TreinSoort + ' naar ' + TussenStations + EindBestemming + ' van ' + VertrekTijd + ' heeft een vertraging van ' + Vertraging + '.']
        #Geen vertragingen in XML data dan dit weeregeven.
        elif 'VertrekVertragingTekst' not in treinRitten:
            Uitvoer_vertragingen += ['Er zijn op dit moment geen vertragingen bekend.']
        break
    print(Uitvoer_vertragingen)
    return Uitvoer_vertragingen

response = requests.get(api_url, auth=auth_details)
dienstRegelingXML = xmltodict.parse(response.text)
vertragingen()


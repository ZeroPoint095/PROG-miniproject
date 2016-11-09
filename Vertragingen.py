#code samengesteld door Roel meijer

import requests
import xmltodict

from API_NS import (auth_details,
                    api_url)

def vertragingen():
    print('Informatie vertragingen: ')
    for treinRitten in dienstRegelingXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        #print('VertrekVertragingTekst' in treinRitten)
        #print(treinRitten)
        if 'RouteTekst' in treinRitten:
            TussenStations = treinRitten['RouteTekst'] + ' met als eindbestemming '
        else:
            TussenStations = ''

        if 'VertrekVertragingTekst' in treinRitten:

                VertrekTijd = treinRitten['VertrekTijd']
                VertrekTijd = VertrekTijd[11:16]
                Vertraging = treinRitten['VertrekVertragingTekst']
                EindBestemming = treinRitten['EindBestemming']
                TreinSoort = treinRitten['TreinSoort']

                print('De ' + TreinSoort + ' naar ' + TussenStations + EindBestemming + ' van ' + VertrekTijd + ' heeft een vertraging van ' + Vertraging + '.')

        elif 'VertrekVertragingTekst' not in treinRitten:
                print('Er zijn op dit moment geen vertragingen bekend.')
        break

response = requests.get(api_url, auth=auth_details)
dienstRegelingXML = xmltodict.parse(response.text)
vertragingen()


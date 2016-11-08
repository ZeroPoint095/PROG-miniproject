#code samengesteld door Roel meijer

import requests
import xmltodict

from API_NS import (auth_details,
                    api_url)

response = requests.get(api_url, auth=auth_details)

dienstRegelingXML = xmltodict.parse(response.text)

def vertragingen():

    for treinRitten in dienstRegelingXML['ActueleVertrekTijden']['VertrekkendeTrein']:

        #print('VertrekVertraging' in treinRitten)
        #print(treinRitten)

        if 'VertrekVertraging' in treinRitten:

                print('De volgende trajecten hebben vertraging:')
                VertrekTijd = treinRitten['VertrekTijd']
                VertrekTijd = VertrekTijd[11:16]
                VertrekVertragingTekst = treinRitten['VertrekVertragingTekst'] # 2016-09-27T18:36:00+0200
                EindBestemming = treinRitten['EindBestemming']
                TreinSoort = treinRitten['TreinSoort']
                RouteTekst = treinRitten['RouteTekst']
                print('De ' + TreinSoort + ' naar ' + RouteTekst + ' met als eindbestemming ' + EindBestemming + ' van ' + VertrekTijd + ' heeft een vertraging van ' + VertrekVertragingTekst + '.')
        else:
                'Er zijn op dit moment geen vertragingen bekend.'

    return vertragingen

vertragingen()

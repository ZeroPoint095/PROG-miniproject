import requests
import xmltodict

email = 'hans1997@gmail.com'
wachtwoord = '8OkOpU2OHYLCQY2RharTmWCjWkKsohv7PtDLLwRq6p1JHPX6DDkWaw'

def actuele_vertrektijden_trein():
    auth_details = (email, wachtwoord)
    api_url = 'https://webservices.ns.nl/ns-api-avt?station=ut'
    response = requests.get(api_url, auth = auth_details)

    vertrekkenXML = xmltodict.parse(response.text)

    print('Hieronder staan de actuele vertrektijden vanaf dit station')

    for vertrek in vertrekkenXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']
        vertrektijd = vertrek['VertrekTijd']
        vertrektijd = vertrektijd[11:16]
        treintype = vertrek['TreinSoort']
        #spoor = []
        print('Om ', vertrektijd, ' vertrekt er een trein (', treintype, ') naar ', eindbestemming, ' vanaf spoor', ' met een eventuele vertraging van: ')

    for vertrek_spoor in vertrekkenXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        if vertrek_spoor['VertrekSpoor']['@wijziging'] is 'false':
            spoor = vertrek['VertrekSpoor']['#text']
        elif vertrek_spoor['VertrekSpoor']['@wijziging'] is 'true':
            spoor = vertrek['VertrekSpoor']['#text']
        print(spoor)
        #route = vertrek['RouteTekst']
        #vertraging = vertrektijden['VertrekVertragingTekst']

    #print('Om ', vertrektijd, ' vertrekt er een trein (', treintype, ') naar ', eindbestemming, ' vanaf spoor', spoor, ' met een eventuele vertraging van: ')

actuele_vertrektijden_trein()

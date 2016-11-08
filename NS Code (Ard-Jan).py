import requests
import xmltodict

def actuel_vertrektijden_trein():
    auth_details = ('email', 'ww')
    api_url = 'https://webservices.ns.nl/ns-api-avt?station=ut'

    response = requests.get(api_url, auth = auth_details)

    with open('actuele_vertrektijden.xml', 'w') as act_avt:
        act_avt.write(response.text)

    
actuel_vertrektijden_trein()

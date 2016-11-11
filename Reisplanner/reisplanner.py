import requests
import xmltodict
from API_NS import (auth_details)
from datetime import datetime

#huidigeStation='Utrecht Centraal'
#bestemming='Gouda'

## offline xml
# with open('offlinetest.xml') as xmlfile:
#    reisplannerXML=xmltodict.parse(xmlfile.read(),dict_constructor=dict)

def reisplannerUitvoeren(huidigeStation, bestemming):
    'Returnt een string met de optimale reis van waarde huidigeStation, bestemming, inclusief eventuele overstap'

    returnString=[]
    api_url = 'http://webservices.ns.nl/ns-api-treinplanner?fromStation='+huidigeStation+'&toStation='+bestemming+'&departure=trueexterne'
    response = requests.get(api_url, auth=auth_details)
    reisplannerXML = xmltodict.parse(response.text)
    def optimaalReis():
        'Returnt de eerste de beste vertrektijd, spoor nummer en treinsoort'
        for xml in reisplannerXML['ReisMogelijkheden']['ReisMogelijkheid']:
            if xml['Optimaal'] == 'true':
                overstap = 0
                overstapStation =[]
                aantalOverstappen = int(xml['AantalOverstappen'])
                while aantalOverstappen != overstap:
                    overstappenIn=xml['ReisDeel'][1]['ReisStop'][0]['Naam']
                    overstapStation.append(overstappenIn)
                    overstap+=1
                tijd=xml['ActueleVertrekTijd'] #actuele vertrektijd volgens de NS API
                tijd=datetime.strptime(tijd, "%Y-%m-%dT%H:%M:%S%z")#converteert ISO tijd naar datetime tijd
                tijd=datetime.strftime(tijd, '%H:%M') #split de tijd in enkel uren en minuten
                #tijdOver=datetime.strftime(tijd, '%H:%M')-datetime.now()
                if overstap >0:
                    spoor=xml['ReisDeel'][0]['ReisStop'][0]['Spoor']['#text']
                    trein=xml['ReisDeel'][0]['VervoerType']
                else:
                    spoor=xml['ReisDeel']['ReisStop'][0]['Spoor']['#text']
                    trein=xml['ReisDeel']['VervoerType']
        return tijd, spoor, trein, overstapStation

    returnString.append(('De eerstevolgende '+optimaalReis()[2]+' trein naar '+bestemming+' vertrekt om '+optimaalReis()[0]+' vanaf spoor '+optimaalReis()[1]+'.'))
    if optimaalReis()[3]!=[]:
        returnString.append('\nU heeft een overstap in: '+(', '.join(optimaalReis()[3])))
    return (''.join(returnString))


# ## mislukte xml parse pogingen ###
# optimaal = reisplannerXML['ReisMogelijkheden']['ReisMogelijkheid']['Optimaal']
# actueleVertrektijd = reisplannerXML['ReisMogelijkheden']['ReisMogelijkheid']['ActueleVertrekTijd']
# vertrekSpoor = reisplannerXML['ReisMogelijkheden']['ReisMogelijkheid']['ReisDeel']['Reisstop']['Spoor']
# overstap = reisplannerXML['ReisMogelijkheden']['ReisMogelijkheid']

def printTest():
    'laat zien de verschillende print mogelijkheden'
    #resultaat als lijst
    print(optimaalReis())
    #resultaat als 3 losse strings
    print(optimaalReis()[0], optimaalReis()[1], optimaalReis()[2])
    #resultaat in een zin
    print('De eerste de beste',optimaalReis()[2],'trein vertrekt om',optimaalReis()[0],'vanaf spoor',optimaalReis()[1])
    if optimaalReis()[3]!=[]:
        print('U heeft een overstap in:',', '.join(optimaalReis()[3]))

### uncomment to run ###
#print(Reisplanner(huidigeStation,bestemming))

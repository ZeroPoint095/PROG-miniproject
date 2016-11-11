import requests
import xmltodict
from API_NS import (auth_details)
from collections import defaultdict

api_url = 'http://webservices.ns.nl/ns-api-stations-v2'
response = requests.get(api_url, auth=auth_details)

ic = xmltodict.parse(response.text)

def makeIntercityStationList():
    icList=[]
    for station in ic['Stations']['Station']:
        if station['Land'] == 'NL':
            if station['Type'] == 'knooppuntIntercitystation' or station['Type'] == 'intercitystation':
                if station['Namen']['Lang'][0]=='\'':
                    icList.append(station['Synoniemen']['Synoniem'][1])
                else:
                    icList.append(station['Namen']['Lang'])
    return icList

def makeIntercityStationDict(icList):
    stationsAlfa = defaultdict(list)
    for station in icList:
        stationsAlfa[station[0]].append(station)
    return stationsAlfa

def returnStations:
    icList=makeIntercityStationList()
    icAlfaDict=makeIntercityStationDict(icList)
    return icAlfaDict   #alle intercity stations met 1e letter als key, alle stations met
                        #de desbetreffende letter als value.

#mislukte code
# from itertools import groupby
# from operator import itemgetter
# from collections import defaultdict


# stationsAlfa=defaultdict(list)
# for letter, station in groupby(sorted(icList), key=itemgetter(0)):
#     for letter, word in icList:
#         stationsAlfa[letter].append(word)



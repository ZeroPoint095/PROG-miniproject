import requests
import xmltodict
from API_NS import (auth_details)

api_url = 'http://webservices.ns.nl/ns-api-stations-v2'
response = requests.get(api_url, auth=auth_details)

ic = xmltodict.parse(response.text)
icList=[]

for station in ic['Stations']['Station']:
    if station['Land'] == 'NL':
        if station['Type'] == 'knooppuntIntercitystation' or station['Type'] == 'intercitystation':
            icList.append(station['Namen']['Lang'])

print(icList)

from itertools import groupby
from operator import itemgetter
from collections import defaultdict

stationsAlfa=defaultdict(list)
for letter, words in groupby(sorted(icList), key=itemgetter(0)):
    for key, value in icList:
        stationsAlfa[key].append(value)
    for word in words:
        lijst_stations_tijdelijk+=[word]
        print (word)
print(stationsAlfa)

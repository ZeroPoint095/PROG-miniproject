import requests
import xmltodict

auth_details = ('hans1997@gmail.com', '8OkOpU2OHYLCQY2RharTmWCjWkKsohv7PtDLLwRq6p1JHPX6DDkWaw')
api_url = 'http://webservices.ns.nl/ns-api-storingen?station=ut'
response = requests.get(api_url, auth=auth_details)

storingenXML = xmltodict.parse(response.text)




storingID = storingenXML['Storingen']['Ongepland']['Storing']['id']
storingTraject = storingenXML['Storingen']['Ongepland']['Storing']['Traject']
storingReden = storingenXML['Storingen']['Ongepland']['Storing']['Reden']
storingBericht = storingenXML['Storingen']['Ongepland']['Storing']['Bericht']
storingIDGepland = storingenXML['Storingen']['Gepland']['Storing']['id']
storingTrajectGepland = storingenXML['Storingen']['Gepland']['Storing']['Traject']
storingPeriodeGepland = storingenXML['Storingen']['Gepland']['Storing']['Periode']
storingBerichtGepland = storingenXML['Storingen']['Gepland']['Storing']['Bericht']

print('Dit zijn de treinen met een ongeplande storing: ')
print(storingTraject)
print('Reden:', storingReden)

print('\n', 'Dit zijn de treinen met een geplande storing: ')
print(storingTrajectGepland)
print('Periode: ', storingPeriodeGepland)






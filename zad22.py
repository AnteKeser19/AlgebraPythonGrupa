import requests
from bs4 import BeautifulSoup
 
URL='https://www.worldometers.info/world-population/'
 
 
wp_stranica=BeautifulSoup(requests.get(URL).content, 'html.parser')
 
svi_podaci=wp_stranica.find_all('p')
print(svi_podaci)
print()
neki_podaci=svi_podaci[14]

print(neki_podaci)

podacistrong=neki_podaci.find('strong').get_text()
print(podacistrong)
# naslovih3=neki_podaci.find('h3').get_text()
# naslovih3=neki_podaci.find_next('h3').get_text()
# print(naslovih3)
# print()
# corona_cases=svi_podaci[0]
# print(corona_cases)
 
# print()
# naslov=corona_cases.find('h1').get_text()
# print(naslov)
# vrijednost=corona_cases.find('span').get_text()
# print(vrijednost)
 
# print()
# for item in svi_podaci:
#     naslov=item.find('h1').get_text()
#     vrijednost=item.find('span').get_text()
#     print(naslov,vrijednost)
 

#pip install BeautifulSoup4

#izvuci horoskop s 24sata

import requests
from bs4 import BeautifulSoup
 
URL='https://www.algebra.hr'
URL2='https://index.hr'
URL3='https://24sata.hr'
URL4='https://phet-dev.colorado.edu/html/build-an-atom/0.0.0-3/simple-text-only-test-page.html'
URL5='https://www.worldometers.info/coronavirus/'
 
#response=requests.get(URL)
# print(response.status_code)
# print()
# print(response.content)
# print()
# print(response.headers)
# print()
# print(response.text)
 
# stranica=BeautifulSoup(response.content,'html.parser')
 
# svi_paragrafi=stranica.find_all('p')
# print(svi_paragrafi)
 
covid_stranica=BeautifulSoup(requests.get(URL5).content, 'html.parser')
 
svi_podaci=covid_stranica.find_all('div', id='maincounter-wrap')
print(svi_podaci)
 
print()
corona_cases=svi_podaci[0]
print(corona_cases)
 
print()
naslov=corona_cases.find('h1').get_text()
print(naslov)
vrijednost=corona_cases.find('span').get_text()
print(vrijednost)
 
print()
for item in svi_podaci:
    naslov=item.find('h1').get_text()
    vrijednost=item.find('span').get_text()
    print(naslov,vrijednost)
 

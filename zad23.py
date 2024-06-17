import requests
from bs4 import BeautifulSoup
 
URL='http://books.toscrape.com/'
 
opis_ocjena={
    "One":1,
    "Two":2,
    "Three":3,
    "Four":4,
    "Five":5
}
 
cijena_selector=".price_color"
naslov_selector=".product_pod h3 a"
ocjena_selector=".star-rating"
 
 
podaci=requests.get(URL).content
sadrzaj=BeautifulSoup(podaci,'html.parser')
 
# print(sadrzaj)
 
cijene=sadrzaj.select(cijena_selector)
naslovi=sadrzaj.select(naslov_selector)
ocjene=sadrzaj.select(ocjena_selector)
 
print(cijene[0].get_text())
print(naslovi[0])
print(naslovi[0]['title'])
print(ocjene[0]['class'][1])
opisna_engleska_ocjena=ocjene[0]['class'][1]
print(opis_ocjena[opisna_engleska_ocjena])
 
print('*'*50)
 
for cijena in cijene:
    print(cijena.get_text())
 
for naslov in naslovi:
    print(naslov['title'])
 
for ocjena in ocjene:
    print(opis_ocjena[ocjena['class'][1]])
 
print()
 
for cijena, naslov, ocjena in zip(cijene, naslovi, ocjene):
    print(f"Knjiga \"{naslov['title']}\" ocjenjena je s {opis_ocjena[ocjena['class'][1]]} zvjezdice, a cijena joj je {cijena.get_text()}")


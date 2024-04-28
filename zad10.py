#od korisnika zatraziti unos broja ocjena koje planira unijeti npr, 7
#koristeci for petlju, 7 puta ponoviti unos nekog broja, i taj broj dodati u praznu listu naziva ocjene
#nakon konacnog unosa, ispisati listu ocjena
#napraviti varijablu suma_ocjena koja ce zbrojit sve ocjene u listi
#napraviti izracun prosjecna_ocjena koja ce podijeliti suma_ocjena s brojem ocjena da dobijemo prosjek


niz_ocjena=[]

for x in range(7):
    ocjena=int(input('Unesite ocjene:' ))
    niz_ocjena.append(ocjena)

print(niz_ocjena)

a = sum(niz_ocjena)
b = a/7
print(a)
print(f'Prosjecna ocjena je: {b}')






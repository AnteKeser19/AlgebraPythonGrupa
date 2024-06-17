#meni sustav
#Naslov
#1. Prosjek ocjena
#2. Statistika ocjena
#3. Najveci broj bodova
#4. Najmanji broj bodova
#0. Izlaz
 
 
#varijanta 1 - rucni rad
print('E-dnevnik')
print('1. Prosjek ocjena')
print('2. Statistika ocjena')
print('3. Najveci broj bodova')
print('4. Najmanji broj bodova')
print('0. Izlaz')
 
print()
#varijanta 2 - lista
#ulazni dio - varijable
naslov='E-dnevnik'
stavke_menija=['1. Prosjek ocjena','2. Statistika ocjena','3. Najveci broj bodova','4. Najmanji broj bodova','0. Izlaz']
#ispisni dio - ovisi o ulazu
print(naslov)
for opcija in stavke_menija:
    print(opcija)
 
print()
#varijanta 3 - lista bez brojeva
#ulazni dio - varijable
naslov='E-dnevnik'
stavke_menija=['Prosjek ocjena','Statistika ocjena','Najveci broj bodova','Najmanji broj bodova','Konfiguracija','Izlaz']
#ispisni dio - ovisi o ulazu
print(naslov)
for indeks, opcija in enumerate(stavke_menija):
    if indeks==len(stavke_menija)-1:
        indeks=-1
    print(f'{indeks+1}. {opcija}')
 
 
 
 
 
#user input v1
# odabir=input('Unesite opciju od 0 do 5: ')
# print(f'Odabrali ste opciju {odabir}')
 
# #user input v2
# odabir=input('Unesite opciju od 0 do 5: ')
# print(f'Odabrali ste opciju {odabir} - {stavke_menija[int(odabir)-1]}')
 
'''
lista "slova"
indeksi     0   1   2   3   4
      -5   -4  -3  -2  -1
vrijednost  a   b   c   d   ne postoji
 
 
int(8bit) -> 0 do 255, ili od 2^0 do sum(2^0 do 2^7) ILI -128 do +127
'''
 
# print()
# slova=['a','b','c','d','e']
# #idemo po slovo c
# print(slova[2])
# print(slova[-3])
 
# #user input v3
# try:
#     odabir=int(input(f'Unesite opciju od 0 do {len(stavke_menija)-1}: '))
#     if odabir>=0 and odabir<len(stavke_menija):
#         print(f'Odabrali ste opciju {odabir} - {stavke_menija[odabir-1]}')
#     else:
#         print('Broj nije u dopustenom rasponu!')
# except ValueError:
#     print('Krivi unos!')
# except:
#     print('Nepoznata greska')
 
 
#user input v4 #hotel california
while True:
    try:
        odabir=int(input(f'Unesite opciju od 0 do {len(stavke_menija)-1}: '))
        if odabir>=0 and odabir<len(stavke_menija):
            print(f'Odabrali ste opciju {odabir} - {stavke_menija[odabir-1]}')
            break
        else:
            print('Broj nije u dopustenom rasponu!')
    except ValueError:
        print('Krivi unos!')
    except:
        print('Nepoznata greska')
#print('You can leave if you know the key')
#print(f'Your key was {odabir}')
print()
 
 
 
#dummy data
lista_ocjena=[3,2,4,4,3,1,5,2,5,5,1,1,2,2,4,4,4,3]
 
#obrada odabira (nekakva funkcionalnost)
#obrada po skolski v1
if odabir==0:
    print('Hvala na koristenju, dovidjenja!')
elif odabir==1:
    print(f'Prosjek ocjena je {sum(lista_ocjena)/len(lista_ocjena):.2f}')
 
#obrada match-case v2
match odabir:
    case 0:
        print('Hvala na koristenju, dovidjenja!')
    case 1:
        print(f'Prosjek ocjena je {sum(lista_ocjena)/len(lista_ocjena):.2f}')
    case 2:
        print(f'Najveca ocjena je {max(lista_ocjena)}')
 
 
#zadatak
#na temelju primjera, posloziti sustav menija:
#naslov: Kucni budjet
#1. Unos place (dodaje placu na ukupni saldo)
#2. Uplata
#3. Isplata (bankomat)
#4. Placanje (kartica)
#5. Ispis stanja
#6. Ispis prometa (kronosloski ispisane sve transakcije +za uplate, -za isplate)
#0. Izlaz
 
 
#domaci rad
#umjesto liste primjeniti dictionary, gdje ce key biti slovo koje oznacava opciju, a value ce biti (barem) puni naziv u meniju s boldanim i potcrtanim slovom (hint... how to...)
#s obzirom na razlicita slova, meni cemo malo promijeniti:
# _U_plata (U)
# _I_splata (I)
# _S_tanje (S)
# _T_ransakcije (T)
# _O_djava (O)
 
# Ispis Trasakcija treba biti u obliku
# R.br.     Uplata      Isplata     Saldo
# 0.                                0.
# 1.        1500                    1500
# 2.                    100         1400
# 3.        200                     1600
# itd.
 
# Ponuditi opciju _Z_adnjih 5 transakcija i _S_ve transakcije odabirom opcije _T_ iz prethodnog menija
 
# Obavijestiti o nemogućnosti isplate ukoliko korisnik pokuša podignuti (potrošiti) više novaca nego ih ima na računu (minimum je 0, osim ako ne želite dodati dopušteni minus)
 
# Stanje samo ispisuje trenutni Saldo
 
# Nakon obavljanja neke od radnji, vraćamo se natrag na početni meni opcijom _P_ovrat na meni ili izlazimo opcijom _O_djava. Vrijedi za sve osim početne opcije Odjava
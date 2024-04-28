Naslov = 'Kucni budzet'
Stavke = ['Unos place', 'Uplata', 'isplata(bankomat)', 'placanje(kartica)', 'Ispis stanja', 'Ispis prometa', 'Izlaz']
print(Naslov)
for indeks, opcija in enumerate(Stavke):
    if indeks == len(Stavke)-1:
        indeks =-1
    print(f'{indeks+1}. {opcija}')

while True:
    try:    
        odabir = int(input(f'Unesite opciju od 0 do {len(Stavke)-1}: '))
        if odabir>= 0 and odabir<len(Stavke):
            print(f'Odabrali ste opciju {odabir} - {Stavke[odabir-1]}')
            break
        else:
            print('Broj nije u dopustenom rasponu')
    except ValueError:
        print('Krivi unos!')
    except:
        print('Nepoznata greska')

KucniBudzet = [5000]
 

if odabir == 0:
        print('Hvala na koristenju.')
elif odabir == 1:
        placa = int(input('Unesi iznos place u eurima: '))
        print(f'Kucni budzet je sada: {sum(KucniBudzet,placa)} eura')
elif odabir == 2:
        uplata = int(input('Koliki je iznos uplate?: '))
        print(f'Kucni budzet je sada: {sum(KucniBudzet,uplata)} eura')
elif odabir == 3:
        isplata = int(input('Koliki je iznos isplate?: '))
        print(f'Kucni budzet je sada: {(KucniBudzet,isplata)}')
elif odabir == 4:
        placanje = int(input('Koliki je iznos placanja?: '))
        print(f'Kucni budzet je sada: {(KucniBudzet,placanje)}')
elif odabir == 5:
        print(f'Stanje kucnog budzeta je {KucniBudzet} eura')






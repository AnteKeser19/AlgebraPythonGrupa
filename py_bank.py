import os  
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
from datetime import date
broj_generiranih_racuna = 0
bankovni_racuni = {}
bankovni_racuni_promet = {}
start_meni = ['Kreiranje racuna Tvrtke', 'Prikaz stanja racuna', 'Prikaz prometa po racunu', 'Polog novca na racun', 'Podizanje novca s racuna', 'Izlaz iz programa']
trenutni_korisnik = ''
izlaz = ''

def provjera_validnosti_oib(oib):
    '''Provjeravamo ispravnost oiba koji korisnik proslijedjuje. Ovaj kod sam posudio od kolege Emila 
    jer u svojem kodu nikako nisam mogao pronaci gdje grjesim.'''
    f=0
    for a in range(len(oib)-1): 
        b=oib[a]
        b=int(b)+f
        c=b+10
        d=c%10
        if d==0:
            d=10
        e=d*2
        f=e%11

        kont_znam=(11-f)%10
        if kont_znam==int(oib[10]):
            return True
        else:
            print('Oib nije validan!')
            return False

def provjera_bankovnog_racuna(bankovni_racuni,ime):
    '''Ovom funocijom provjeravamo postoji li u dictionaryu bankovni_racuni vec bankovni racun na ime tvrtke
    na koju korisnik zeli otvoriti racun. Ukoliko vec postoji racun na tu tvrtku, korisniku ne dajemo da nastavi
    s kreiranjem racuna.'''
    for value in bankovni_racuni.values():
            for value in value.values():
                if value == ime:
                    return False
    

def kreiranje_računa():
    '''Pomocu ove funkcije od korisnika trazimo da unese sve trazene podatke:ime_tvrtke,adresu,kucni broj
    postanski broj, grad sjediste i oib. Ukoliko bilo koja varijabla od navedenih nije ispravna, trazimo
    od korisnika da ponovno unese varijablu. Tek kada je sve ispravno, vracamo varijable u obliku liste.'''
    while True:
        ime_tvrtke = input('Unesi ime na koje zelis otvoriti racun: ').capitalize()
        provjera = provjera_bankovnog_racuna(bankovni_racuni,ime_tvrtke)
        if provjera == False:
            print('Za navedenu tvrtku vec postoji otvoreni racun!')
            continue
        if len(ime_tvrtke) <2:
                    print('Ime mora sadrzavati minimalno 2 znaka!')
                    continue
        else:
            while True:
                sjediste = input('Unesi:(Ulica,kucni broj,postanski broj,grad sjedista) ').split(',')
                print()
                vlasnik = input('Unesi ime i prezime vlasnika: ').split()
                print()
                if len(sjediste) != 4 or len(vlasnik) <2:
                    print('Krivi unos!')
                    continue
                if sjediste[1].isnumeric() == False or int(sjediste[1]) > 500:
                    print('Adresa nije valjana!')
                    continue
                if sjediste[1].isnumeric() == False or int(sjediste[2]) not in range(10000,53297):
                    print('Adresa nije valjana!')
                    continue
                if len(sjediste[3]) < 3:
                    print('Adresa nije valjanja')
                    continue
                else:
                    for stavka in sjediste:
                        sjediste[sjediste.index(stavka)] = stavka.capitalize()
                    for stavka in vlasnik:
                        vlasnik[vlasnik.index(stavka)] = stavka.capitalize()
                    while True:
                        oib = input('Unesi oib: ')
                        try:
                            oib = int(oib)
                            oib = str(oib)
                        except:
                            ValueError
                            print('Oib mora biti broj!')
                            continue
                        print()
                        if len(oib) < 11:
                            print('OIB mora sadrzavati minimalno 11 znamenki!')
                            continue
                        if provjera_validnosti_oib(oib) == False:
                            continue
                        else:
                            while True:
                                try:
                                    iznos = int(input('Koji iznos zelite poloziti? '))
                                    if iznos < 100:
                                        print('Morate poloziti minimalno 100€')
                                        continue
                                    else:
                                        print()
                                        print(f'Polozili ste {iznos}€.')
                                        break
                                except:
                                    ValueError
                                    print('Krivi unos!')
                                    continue
                            break
                    break
            break
    return [ime_tvrtke] + sjediste + vlasnik + [oib],iznos

def generiraj_racun(korisnicki_podaci,saldo):
    '''U ovu funkciju proslijedjujemo podatke iz funkcije kreiranje_racuna te navedene podatke sparujemo s odgovarajucim stringom
    koji opisuje taj podatak. Zatim te podatke spremamo kao key:value u dict. Ti podaci zatim postaju sami po sebi dictionary koji je
    value u dictionaryu u kojem nam je key naziv samog racuna. Naziv racuna dobivamo prema uputama iz zadatka koristeci funkciju datetime.
    Isto tako, stvaramo dva dictionarya, jedan cuva podatke o korisniku racuna, a drugi o prometu na bankovnom racunu. Mogao sam mozda to sve
    staviti u jedan dict, no cinilo mi se malo kompliciranim.'''
    global broj_generiranih_racuna,bankovni_racuni,bankovni_racuni_promet,trenutni_korisnik
    broj_generiranih_racuna += 1
    dictionary_keyes = ['ime tvrtke', 'adresa', 'kucni_broj', 'postanski broj', 'grad', 'ime_vlasnika', 'prezime_vlasnika', 'OIB']
    lista_prometa = ['Stanje', 'Promet', 'Polozi' , 'Isplate']
    dictionary_prometa = {}
    dictionary_podataka = {}
    counter = 0
    for stavka in lista_prometa:
        dictionary_prometa.update({stavka : []})
        if stavka == 'Stanje':
            dictionary_prometa.update({stavka : 0})
        counter +=1
    counter = 0
    datum = date.today()
    for podatak in korisnicki_podaci:
        dictionary_podataka.update({dictionary_keyes[counter] : podatak})
        counter +=1
    if broj_generiranih_racuna < 10000:
        brojac_racuna = f'{broj_generiranih_racuna:05d}'
    else:
        brojac_racuna = broj_generiranih_racuna
    bankovni_racuni.update({f'BA-{datum}-{brojac_racuna}' : None})
    bankovni_racuni[f'BA-{datum}-{brojac_racuna}'] = dictionary_podataka
    bankovni_racuni_promet.update(bankovni_racuni)
    bankovni_racuni_promet[f'BA-{datum}-{brojac_racuna}'] = dictionary_prometa
    trenutni_korisnik = f'BA-{datum}-{brojac_racuna}'
    dict_update(bankovni_racuni_promet,saldo,kljuc = 'Stanje')
    print(bankovni_racuni,bankovni_racuni_promet,sep='\n')
    return

def meni(meni_lista):
    '''Ispisujemo meni sa zeljenim stavkama.'''
    print('*'*20,'M E N I','*'*20)
    for rb,stavka in enumerate(meni_lista):
        if rb == len(meni_lista) -1:
            rb = -1
        print(f'\t\t{rb+1}. {stavka}')

def odabir_opcije(meni_lista):
    '''Od korisnika trazimo odabir neke od ponudjenih opcija koje se prikazuju kroz funkciju meni.'''
    max_opcija=len(meni_lista)-1
    while True:
        try:
            opcija=int(input(f'Unesi opciju od 0 do {max_opcija}: '))
        except:
            print(f'Krivi unos!')
            continue
        if opcija>=0 and opcija<=max_opcija:
            return opcija

def provjera_opcije(opcija):
    '''Provjeravamo koju je opciju korisnik odabrao i sukladno tome vrtimo odgovarajuci dio koda.'''
    if opcija == 1:
        korisnicki_podaci, saldo = kreiranje_računa()
        generiraj_racun(korisnicki_podaci,saldo)
    elif opcija == 2:
        while True:
            if trenutni_korisnik == '':
                print('Vas racun jos ne postoji, prvo kreirajte racun!')
                input()
                break
            else:
                kljuc = 'Stanje'
                ispis = dohvacanje_podataka_dict(bankovni_racuni_promet,trenutni_korisnik,kljuc)
                print(f'Vase stanje racuna iznosi {ispis}€')
                input()
                break
    elif opcija == 3:
        while True:
            if trenutni_korisnik == '':
                print('Vas racun jos ne postoji, prvo kreirajte racun!')
                input()
                break
            else:
                kljuc = 'Promet'
                ispis = dohvacanje_podataka_dict(bankovni_racuni_promet,trenutni_korisnik,kljuc)
                ispis_prometa(ispis)
                input()
                break
    elif opcija == 4:
        while True:
            kljuc = 'Polozi'
            if trenutni_korisnik == '':
                print('Vas racun jos ne postoji, prvo kreirajte racun!')
                input()
                break
            else:
                try:
                    unos = int(input('Koji iznos zelite poloziti? '))
                except:
                    ValueError
                    print('Iznos mora biti broj!')
                if unos < 0:
                    print('Zelite uplatiti novac!')
                else:
                    saldo = bankovni_racuni_promet[trenutni_korisnik]['Stanje']
                    dict_update(bankovni_racuni_promet,saldo,kljuc,unos)
                    print(f'Polozili ste {unos}€')
                    input()
                    break
            

    elif opcija == 5:
        while True:
            kljuc = 'Isplate'
            try:
                if trenutni_korisnik == '':
                    print('Vas racun jos ne postoji, prvo kreirajte racun!')
                    input()
                    break
                unos = int(input('Koji iznos zelite isplatiti? '))
                saldo = bankovni_racuni_promet[trenutni_korisnik]['Stanje']
                if saldo < unos:
                    print('Nedovoljan iznos na racunu!')
                else:
                    dict_update(bankovni_racuni_promet,saldo,kljuc,unos)
                    print(f'Isplatili ste {unos}€')
                    input()
                    break
            except:
                ValueError
                print('Iznos mora biti broj!')

def dohvacanje_podataka_dict(dictionary,ime_racuna,kljuc):
    if ime_racuna in dictionary.keys():
        ispis = dictionary[ime_racuna][kljuc]
        return ispis

def dict_update(dictionary,saldo,kljuc,transakcija=0):
    '''U ovu funkciju proslijedjujemo podatke o transakcijama koje je korisnik proveo te sukladno tome
    azuriramo zeljeni dictionary.'''
    global bankovni_racuni_promet
    opcije = ['Stanje', 'Polozi', 'Isplate','Promet']
    for value in dictionary.values():
        for key in value.keys():
            if key == opcije[0] and opcije[0] == kljuc:
                value[kljuc] += saldo
            if key == opcije[1] and opcije[1] == kljuc:
                value[kljuc].append(transakcija)
                value[opcije[3]].append(transakcija)
                value[opcije[0]] += transakcija
            if key == opcije[2] and opcije[2] == kljuc:
                value[kljuc].append(transakcija)
                value[opcije[3]].append(transakcija)
                value[opcije[0]] -= transakcija
    return

def ispis_prometa(racuni):
    '''Ova funkcija sluzi nam kako bi ispisali dosadanji promet na racunu korisnika u obliku tablice.
    Tablica nije bas savrsena i ima nekih problema no vise-manje je funkcionalna.'''
    print()
    print(f'\tPromet racuna: {trenutni_korisnik}')
    print()
    print('\t''Transakcije','Uplate','Isplate', sep='\t\t')
    print()
    for i in racuni:
        if i in bankovni_racuni_promet[trenutni_korisnik]['Polozi']:
            print(racuni.index(i)+1,i,'\t',i,sep='\t')
            print()
        elif i in bankovni_racuni_promet[trenutni_korisnik]['Isplate']:
            print(racuni.index(i)+1,i,'\t\t\t',i,sep='\t')
            print()
        else:
            print(racuni.index(i)+1,i,sep='\t')
            print()
    input()


#glavni dio#
while True:
    clear()
    meni(start_meni)
    print()
    opcija = odabir_opcije(start_meni)
    if opcija == 0:
        break
    else:
        provjera_opcije(opcija)
        input()
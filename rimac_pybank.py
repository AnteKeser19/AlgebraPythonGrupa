import os
import time
import random
from datetime import datetime

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # u c/c++ (os.name=='nt')?os.system('cls'):os.system('clear')
 
def prikaz_menija(meni):
    print()
    for rb,stavka in enumerate(meni):
        print(f'     {rb}. {stavka}')

def krivi_unos(meni):
    print(f'\033[1mMolimo unesite broj od 0 do {len(meni)-1}!\033[0m\n')
    time.sleep(1)

def repetitivni_koraci(broj):
    d = broj % 10
    if d == 0:
        d = 10
    e = d * 2
    f = e % 11
    return f

def provjera_oib():
    while True:
        oib_za_provjeru=input('Unesite OIB tvrtke: ')
        if not oib_za_provjeru.isdigit():
            print('OIB treba biti u brojcanom obliku!')
            continue
        if len(oib_za_provjeru) != 11:
            print('Broj znamenki u OIB-u treba biti 11!')
            continue
        kontrolna_znamenka = int(oib_za_provjeru[10])
        zadnji_korak = []
        for i in range(len(oib_za_provjeru)-1):
            if i == 0:
                c = int(oib_za_provjeru[i]) + 10
                f = repetitivni_koraci(c)
                zadnji_korak.append(f)
            else:
                c = int(oib_za_provjeru[i]) + zadnji_korak[i-1]
                f = repetitivni_koraci(c)
                zadnji_korak.append(f)
        provjera = 11 - zadnji_korak[9]
        if provjera == 10:
            provjera = 0
        if provjera == kontrolna_znamenka:
            #print(f'OIB {oib_za_provjeru} je valjan!')
            return oib_za_provjeru
        else:
            print(f'OIB {oib_za_provjeru} nije valjan!')
            continue

def posta():
    while True:
        try:
            posta=int(input('Unesite postanski broj sjedista tvrtke: '))
        except:
            print('Postanski broj mora biti peteroznamekasti broj!')
            time.sleep(1)
            continue
        if not 10000<=posta<=99999:
            print('Postanski broj mora biti peteroznamekasti broj!')
            continue
        else:
            break


def kreiranje_racuna():
    global trenutno_stanje
    while True:
        clear()
        print('Odabrali ste \033[1mKreiraj racun tvrtke\033[0m!')
        racun['Naziv']=input('Unesite naziv tvrtke: ')
        if len(racun['Naziv'])<1:
            continue
        racun['Adresa']=input('Unesite adresu (ulicu i broj) tvrtke: ')
        posta()
        racun['Grad']=input('Unesite grad sjedista tvrtke: ')
        racun['OIB']=provjera_oib()
        racun['Ime i prezime vlasnika']=input('Unesite ime i prezime odgovorne osobe: ')
        broj = "%05d" % random.randint(0,99999)
        racun['Broj racuna']='BA-'+str(datetime.now().month)+'-'+str(datetime.now().year)+'-'+broj
        print('Uspjesno ste unijeli sve podatke.')
        print(f'\nNaziv tvrtke: {racun["Naziv"]}\nAdresa tvrtke: {racun["Adresa"]}\nPostanski broj i grad: {racun["Posta"]} {racun["Grad"]}\nOIB: {racun["OIB"]}\nBroj racuna: {racun["Broj racuna"]}')
        while True:
            try:
                uplata=float(input('\nZa otvaranje racuna polozite iznos po volji: '))
            except:
                print('Molimo unesite iznos u brojkama!')
                continue
            if uplata<=0:
                print('Molimo unesite pozitivan iznos!')
                continue
            trenutno_stanje+= uplata
            povijest.append((uplata, '', trenutno_stanje))
            print(f'Uplatili ste \033[1m{uplata:.2f} EUR\033[0m!. Trenutno stanje je: \033[1m{trenutno_stanje:.2f} EUR\033[0m!.')
            ponovna_uplata=input('Zelite li izvrsiti jos jednu uplatu? (d/n): ')
            if ponovna_uplata=='d':
                continue
            else:
                print('\nPovratak na pocetni meni.')
                time.sleep(1)
                clear()
                break
        break


def prikaz_stanja():
    clear()
    print('Odabrali ste \033[1mPrikaz stanja racuna\033[0m!')
    print(f'Racun broj: \033[1m{racun["Broj racuna"]}\033[0m')
    print(f'Trenutno stanje je \033[1m{trenutno_stanje} EUR\033[0m!')
    input('\nZa povratak pritisnite bilo koji gumb: ')
    clear()

def prikaz_prometa():
    clear()
    print('Odabrali ste \033[1mPrikaz prometa racuna\033[0m!')
    print(f'Racun broj: \033[1m{racun["Broj racuna"]}\033[0m')
    print('{:>5} {:>15} {:>15} {:>15}'.format('R.br.','Uplata', 'Isplata','Saldo'))
    for redni_broj, pov in enumerate(povijest):
        print(f'{redni_broj:>5} {pov[0]:>15} {pov[1]:>15} {float(pov[2]):>15,.2f}')
    input('\nZa povratak pritisnite bilo koji gumb: ')
    clear()


def polog_novca():
    
    global trenutno_stanje
    clear()
    print('Odabrali ste \033[1mPolog novca na racun\033[0m!')
    print(f'Racun broj: \033[1m{racun["Broj racuna"]}\033[0m')
    while True:
        try:
            uplata=float(input('\nUnesite iznos uplate: '))
        except:
            print('Molimo unesite iznos u brojkama!')
            continue
        if uplata<=0:
            print('Molimo unesite pozitivan iznos!')
            continue
        trenutno_stanje += uplata
        povijest.append((uplata, '', trenutno_stanje))
        print(f'Uplatili ste \033[1m{uplata:.2f} EUR\033[0m!. Trenutno stanje je: \033[1m{trenutno_stanje:.2f} EUR\033[0m!.')
        ponovna_uplata=input('Zelite li izvrsiti jos jednu uplatu? (d/n): ')
        if ponovna_uplata=='d':
            continue
        else:
            print('\nPovratak na pocetni meni.')
            time.sleep(1)
            clear()
            break
        

def podizanje_novca():
    global trenutno_stanje
    clear()
    print('Odabrali ste \033[1mPodizanje novca s racuna\033[0m!')
    print(f'Racun broj: \033[1m{racun["Broj racuna"]}\033[0m')
    while True:
        try:
            isplata=float(input('\nUnesite iznos isplate: '))
        except:
            print('Molimo unesite iznos u brojkama!')
            continue
        if isplata<=0:
            print('Molimo unesite pozitivan iznos!')
            continue
        if isplata > trenutno_stanje:
            print('Isplata ne moze biti veca od stanja na racunu.')
            time.sleep(1)
            continue
        trenutno_stanje -= isplata
        povijest.append(('', isplata, trenutno_stanje))
        print(f'Podigli ste \033[1m{isplata:.2f} EUR\033[0m!. Trenutno stanje je: \033[1m{trenutno_stanje:.2f} EUR\033[0m!.')
        ponovna_isplata=input('Zelite li izvrsiti jos jednu isplatu? (d/n): ')
        if ponovna_isplata=='d':
            continue
        else:
            print('\nPovratak na pocetni meni.')
            time.sleep(1)
            clear()
            break

glavni_meni=['Izadji iz programa', 'Kreiraj racun tvrtke', 'Prikazi stanje racuna', 'Prikazi promet po racunu', 'Polozi novce na racun', 'Podigni novce s racuna']

povijest = [('', '', 0), (150, '', 150), ('', 30, 120), ('', 70, 50), (65,'', 115), ('', 25, 90), (300, '', 390)]
trenutno_stanje=390

racun={'Naziv': '',
       'Adresa':'',
       'Posta':'',
       'Grad':'',
       'OIB':'',
       'Ime i prezime vlasnika':'',
       'Broj racuna':''
}



while True:
    clear()
    print()
    print('*'*10,'Dobrodosli u','*'*10,'\n','*'*9,'   PyBank    ','*'*9)
    prikaz_menija(glavni_meni)
    try:
        odabir=int(input(f'\nMolimo odaberite jednu od sljedecih opcija (0-{len(glavni_meni)-1}): '))
    except:
        krivi_unos(glavni_meni)
        continue
    if odabir>(len(glavni_meni)-1):
        krivi_unos(glavni_meni)
        continue
    elif odabir==0:
        print('\nZahvaljujemo na koristenju!\n')
        break
    elif odabir==1:
        kreiranje_racuna()
    elif odabir==2:
        prikaz_stanja()
    elif odabir==3:
        prikaz_prometa()
    elif odabir==4:
        polog_novca()
    elif odabir==5:
        podizanje_novca()


    
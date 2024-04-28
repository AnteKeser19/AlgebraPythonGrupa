def prikaz_menija(meni):
    print("\n===== MENI =====")
    for key, value in meni.items():
        print(f"\033[1m\033[4m{key}\033[0m: {value}")

def uplata(stanje_racuna, povijest_transakcija):
    '''
    Ova funkcija vrši uplate na račun. Od korisnika se očekuje da upiše iznos uplate, te će ta uplata
    biti zbrojena s predefiniranim stanjem računa (pogledaj varijablu stanje računa). Te će u listu
    povijest transakcija dodati tu uplatu, njen iznos i promijenjeno stanje računa.
    '''
    uplata = float(input('Unesite iznos uplate: '))
    stanje_racuna += uplata
    print(f'Uspjesno ste uplatili {uplata} eura. Novo stanje računa je: {stanje_racuna} eura.')
    povijest_transakcija.append(['Uplata', uplata, stanje_racuna])
    return stanje_racuna, povijest_transakcija

def isplata(stanje_racuna, povijest_transakcija):
    '''
    Ova funkcija vrši isplatu s račnua. Od korisnika će zatražiti unos isplate, te UKOLIKO JE MOGUĆE izvršit će tu isplatu
    na način da će sa predefiniranog stanja računa (pogledaj varijablu stanje računa) oduzeti uneseni iznos.

    Te će u listu "povijest transakcija" dodati tu isplatu, njen iznos i promijenjeno stanje računa.

    Ukoliko nije moguće izvršiti isplatu korisnik će zaprimiti poruku kako nema dovoljno sredstava na računu. - Program će nastaviti s radom.
    '''
    isplata = float(input("Unesite iznos isplate: "))
    if isplata > stanje_racuna:
        print("Nemate dovoljno sredstava na računu za ovu isplatu.")
    else:
        stanje_racuna -= isplata
        povijest_transakcija.append(['Isplata', isplata, stanje_racuna])
        print(f"Uspješno ste isplatili {isplata} eura. Novo stanje računa: {stanje_racuna} eura.")
    return stanje_racuna, povijest_transakcija


def lista_transakcija(povijest_transakcija):
    '''
    Ova funkcija ispisuje povijest svih transakcija koje su unešene u tu listu (putem uplate i isplate).
    Korištenjem string formatinga ispisuje se u obliku tablice.
    '''
    print('Povijest transakcija:')
    print('{:<10} {:<10} {:<10} {:<15}'.format('Redni broj', 'Tip', 'Iznos', 'Stanje racuna'))
    for rbr, transakcija in enumerate (povijest_transakcija, 1):
        tip, iznos, stanjeracuna = transakcija
        print('{:<10} {:<10} {:<10} {:<15}'.format(rbr, tip, iznos, stanjeracuna))


stanje_racuna = 5000

meni = {
    'U': ['Uplata'],
    'I': ['Isplata'],
    'S': ['Stanje'],
    'T': ['Transakcije'],
    'O': ['Odjava']
}

povijest_transakcija = []

while True:
    prikaz_menija(meni)
    opcija = input("Odaberite opciju: ").upper()
    if opcija not in meni:
        print("Nevažeća opcija, molimo pokušajte ponovno.")
        continue

    if opcija == 'U':
        stanje_racuna, povijest_transakcija = uplata(stanje_racuna, povijest_transakcija)

    elif opcija == 'I':
        stanje_racuna, povijest_transakcija = isplata(stanje_racuna, povijest_transakcija)

    elif opcija == 'S':
        print(f"Trenutno stanje računa: {stanje_racuna} eura.")

    elif opcija == 'T':
        lista_transakcija(povijest_transakcija)



    elif opcija == 'O':
        print("Hvala na korištenju. Doviđenja!")
        break

    print('Odaberite jednu od ponudjenih opcija')
    print('1: Povratak na početni meni')
    print('2: Zatvaranje programa')
    PovratakNaMeni =  input("Odaberite opciju: ")
    if PovratakNaMeni == '1':
        continue
    elif PovratakNaMeni == '2':
        print("Hvala na korištenju. Doviđenja!")
        break
    else:
        print('Nevazeca opcija.')
        continue

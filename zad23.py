# beskonacna petlja
# x za izlaz
# u za unos imena
# i za ispis dobivenog imena
 
# u - provjerava duzinu imena, pa ako je manja od 2 slova, trazi ponovni unos
# nakon ispravnog unosa vraca prihvaceno ime
 
# i - prima jednu vrijednost (ime), i ispisuje poruku "Dobar dan {ime}!"
 
# x - break outa iz while petlje
 
ime = ''
 
def meni():
    print('\n\033[1m-----MENI-----\033[0m')
    print('u: Unos imena')
    print('i: Ispis imena')
    print('x: Izlaz')
 
def unos():
    global ime
    while True:
        ime = input('Molimo unesite ime: ').capitalize()
        if len(ime) < 2:
            continue
        else:
            break
 
def ispis(ime):
    print(f'Dobar dan, {ime}!')
 
while True:
    meni()
    odabir = input('Unesite zeljenu opciju: ').lower()
    print()
    if odabir == 'x':
        break
    elif odabir == 'u':
        unos()
    elif odabir == 'i':
        ispis(ime)
    else:
        print('Molimo unesite validan izbor!')

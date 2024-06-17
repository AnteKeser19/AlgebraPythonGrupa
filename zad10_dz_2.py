# Kao temelj domaceg uzimamo prikaz racuna i njegov ispis (prethodna predavanja)
# Za datum racuna uzeti datetime, datum, ukljucujuci i vrijeme (samo H i M)
# Neka dio broja racuna ukljucuje kombinaciju datuma i vremena + iteraciju od 0000 do 9999
# Kreirati klasu Proizvod koja će minimalno imati njegov naziv i cijenu (po zelji prosiriti opisom itd.)
# Kreirati klasu Racun koja ce imati stavke datum, br_racuna, lista_stavki-br_kom_za_stavke, sve dodatno po potrebi)
# Kreirati metodu ispis() koja klase Racun koja ce pozivom nad objektom Racuna ispisati konkretni racun
# Napraviti class metodu ukupan_broj_racuna koja ce vratiti broj izdanih racuna (ili npr. samo isprintani) 

# jos treba zamijeniti opci PDV s individualnim PDV-om

import datetime as dt
import random

class Proizvod():
    def __init__(self, neto_cijena, iznos_pdv):
        self.neto_cijena=neto_cijena
        self.iznos_pdv=iznos_pdv

    def cijena(self):
        return(self.neto_cijena)


class Racun:
    counter=0
    def __init__(self, racun_broj, racun_datum, racun_stavke, racun_iznos_pdv=0.25):
        Racun.counter+=1
        self.racun_broj = racun_broj
        self.racun_datum = racun_datum
        self.racun_stavke = racun_stavke  # {proizvod: (kolicina, ukupna_cijena)}
        self.racun_neto = 0  # ovo je neto iznos u eurima
        self.racun_iznos_pdv = racun_iznos_pdv  # ovo je vrijednost pdv izrazena brojkom (0.25 = 25%)
        self.izracunaj_ukupno_neto()
    
    @classmethod
    def ukupan_broj_racuna(cls):
        return(cls.counter)
    
    def izracunaj_ukupno_neto(self):
        for kolicina, ukupna_cijena in self.racun_stavke.values():
            self.racun_neto += ukupna_cijena

    def izracunaj_iznos_pdv(self):
        return self.racun_neto * self.racun_iznos_pdv  # neto*pdv = 100*0.25

    def ispisi_racun(self):
        print()
        print('*' * 60)
        print(f'\n\tRacun:\t\t{self.racun_broj}')
        print(f'\tDatum:\t\t{self.racun_datum}\n')
        print('-' * 60)
        print('\n\tProizvod\tKolicina\tCijena')
        for proizvod, (kolicina, ukupna_cijena) in self.racun_stavke.items():
            print(f'\t{proizvod:<10}\t{kolicina:<10}\t{ukupna_cijena} EUR')
        print()
        print('-' * 60)
        print(f'\n\tIznos bez PDV:\t\t\t{self.racun_neto:.2f} EUR')
        print(f'\tIznos PDV-a:\t\t\t{self.izracunaj_iznos_pdv():.2f} EUR')
        print(f'\tIznos sa PDV:\t\t\t{(self.racun_neto + self.izracunaj_iznos_pdv()):.2f} EUR')
        print()
        print('*' * 60)

    def sacuvaj_racun(self):
        racun_str = []
        racun_str.append('\n' + '*' * 60)
        racun_str.append(f'\n\tRacun:\t\t{self.racun_broj}')
        racun_str.append(f'\tDatum:\t\t{self.racun_datum}\n')
        racun_str.append('-' * 60)
        racun_str.append('\n\tProizvod\tKolicina\tCijena')
        for proizvod, (kolicina, ukupna_cijena) in self.racun_stavke.items():
            racun_str.append(f'\t{proizvod:<10}\t{kolicina:<10}\t{ukupna_cijena} EUR')
        racun_str.append('\n' + '-' * 60)
        racun_str.append(f'\n\tIznos bez PDV:\t\t\t{self.racun_neto:.2f} EUR')
        racun_str.append(f'\tIznos PDV-a:\t\t\t{self.izracunaj_iznos_pdv():.2f} EUR')
        racun_str.append(f'\tIznos sa PDV:\t\t\t{(self.racun_neto + self.izracunaj_iznos_pdv()):.2f} EUR')
        racun_str.append('\n' + '*' * 60)
        return '\n'.join(racun_str)
 
def kreiraj_racun(pdv):
    racun_stavke = {}
    broj = "%04d" % random.randint(0, 99)
    racun_broj = f'R-{dt.datetime.now().strftime("%Y%m")}-{broj}'
    racun_datum = dt.datetime.now().strftime("%d.%m.%Y., %H:%M")
    while True:
        proizvod = input('Unesite naziv proizvoda ili "n" za izlaz: ')
        if proizvod.lower() == 'n':
            break
        if proizvod in products:
            cijena = products[proizvod].cijena()
            if proizvod in racun_stavke:
                kolicina, ukupna_cijena = racun_stavke[proizvod]
                racun_stavke[proizvod] = (kolicina + 1, ukupna_cijena + cijena)
            else:
                racun_stavke[proizvod] = (1, cijena)
        else:
            print('Artikl nije u ponudi')
            continue
        izlaz = input('Nova stavka d/n? ')
        if izlaz.lower() == 'n':
            break
    racun = Racun(racun_broj, racun_datum, racun_stavke, pdv)
    with open(f'{racun_broj}.txt', 'w') as f:
        f.write(racun.sacuvaj_racun())
    return racun

products = {
    'kruh': Proizvod(1.5, 0.1),
    'mlijeko': Proizvod(0.89, 0.2),
    'novine': Proizvod(0.4, 0.3),
    'cigarete': Proizvod(4.3, 0.25)
}

racuni=[]
PDV=0.25
 
while True:
    racun=kreiraj_racun(PDV)
    racuni.append(racun)
 
    izlaz=input('Novi racun d/n? ')
    if izlaz.lower()=='n':
        break
 
for r in racuni:
    r.ispisi_racun()

for r in racuni:
    print(f'Stvoren je racun {r.racun_broj}.')

if Racun.ukupan_broj_racuna()==1:
    print(f'Stvoren je {Racun.ukupan_broj_racuna()} racun.')
elif 1<Racun.ukupan_broj_racuna()<5:
    print(f'Stvorena su {Racun.ukupan_broj_racuna()} racuna.')
else:
    print(f'Stvoreno je {Racun.ukupan_broj_racuna()} racuna.')
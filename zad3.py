class Racun():
    '''Upravljanje racunom kao objektom'''
    def __init__(self, racun_broj, racun_datum, racun_stavke, racun_iznos_pdv=0.25):
        self.racun_broj=racun_broj
        self.racun_datum=racun_datum
        self.racun_stavke=racun_stavke
        self.racun_neto=0 #ovo je neto iznos u eurima
        self.racun_iznos_pdv=racun_iznos_pdv #ovo je vrijednost pdv izrazena brojkom (0.25 = 25%)
        self.izracunaj_ukupno_neto()
 
    def izracunaj_ukupno_neto(self):
        for stavka in self.racun_stavke.values():
            self.racun_neto+=stavka
 
    def izracunaj_iznos_pdv(self):
        # print(self.racun_neto*self.racun_iznos_pdv)
        return self.racun_neto*self.racun_iznos_pdv # neto*pdv = 100*0.25
 
 
    def ispisi_racun(self):
        print()
        print('*'*50)
        print(f'\n\tRacun:\t\t{self.racun_broj}')
        print(f'\tDatum:\t\t{self.racun_datum}\n')
        print('-'*50)
        print('\n\tProizvod\t\tCijena')
        for proizvod, cijena in self.racun_stavke.items():
            print(f'\t{proizvod:<20}\t{cijena:<10}')
        print()
        print('-'*50)
        print(f'\n\tIznos bez PDV:\t\t{self.racun_neto:.2f}')
        #temp=self.izracunaj_iznos_pdv()
        print(f'\n\tIznos PDV-a:\t\t{self.izracunaj_iznos_pdv():.2f}')
        print(f'\n\tIznos sa PDV:\t\t{(self.racun_neto+self.izracunaj_iznos_pdv()):.2f}')
        print()
        print('*'*50)
 
 
 
'''
racun_broj='R-1-2024-01'
racun_datum_izdavanja='14.05.2024'
racun_stavke={
    'Mlijeko':1.35,
    'Kruh':1.5,
    'Zimska':18.3,
    'Gouda':8.90
}
 
 
 
novi_racun=Racun(racun_broj,racun_datum_izdavanja,racun_stavke)
novi_racun.ispisi_racun()
'''
 
def kreiraj_racun(brrac, pdv):
    racun_stavke={}
    racun_broj=f'R-{brrac}-2024-05'
    racun_datum=input('Unesite datum: ')
    while True:
        proizvod=input('Unesite naziv proizvoda: ')
        cijena=float(input('Unesite cijenu proizvoda'))
        racun_stavke[proizvod]=cijena
        izlaz=input('Nova stavka d/n? ')
        if izlaz.lower()=='n':
            break
    racun=Racun(racun_broj, racun_datum, racun_stavke, pdv)
    return racun
 
 
racuni=[]
PDV=0.25
brojac_racuna=1
 
while True:
    racun=kreiraj_racun(brojac_racuna, PDV)
    brojac_racuna+=1
    racuni.append(racun)
 
    izlaz=input('Novi racun d/n? ')
    if izlaz.lower()=='n':
        break
 
for r in racuni:
    r.ispisi_racun()
 
 
 
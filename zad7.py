# netko=Osoba(ime, oib, email, telefon, adresa)
# d = Djelatnik(ime, prezime, oib, email, telefon, adresa, radno_mjesto)
# k = Kupac(naziv, oib, email, telefon, sjediste, djelatnost)
 
 
class Osoba:
    def __init__(self, ime, oib, mail, telefon, adresa):
        self.ime = ime
        self.oib = oib
        self.email = mail
        self.telefon = telefon
        self.adresa = adresa
 
    def ispis(self):
        print()
        print(self.ime)
        print(self.oib)
        print(self.email)
        print(self.telefon)
        print(self.adresa)
 
ime='Mate'
osoba_a=Osoba(ime,12345678901, 'mate@net.hr','+385921234567','Split')
 
print(osoba_a.ime)
 
 
 
class Djelatnik(Osoba):
    def __init__(self, ime, prezime, oib, email, telefon, adresa, radno_mjesto):
        super().__init__(ime, oib, email, telefon, adresa)
        self.prezime = prezime
        self.radno_mjesto = radno_mjesto
 
    def ispis(self):
        print()
        print(self.ime)
        print(self.prezime)
        print(self.oib)
        print(self.email)
        print(self.telefon)
        print(self.adresa)
        print(self.radno_mjesto)
 
 
djelatnik_b=Djelatnik('Jure','Juric',56734587622,'jjuric@brzi.hr','+385912345678','Zadar','Prodavac')
print(djelatnik_b.email)
 
 
 
class Kupac(Osoba):
    def __init__(self, naziv, oib, email, telefon, sjediste='', djelatnost=''):
        Osoba.__init__(self, naziv, oib, email, telefon, sjediste)
        self.djelatnost = djelatnost
 
    def ispis(self):
        super().ispis()
        print(self.djelatnost)
 
 
kupac_c=Kupac('Stipe',4786378428310,'stipe@info.hr','+385256374895673','Pozega','nesto')
print(kupac_c.adresa)
 
 
osoba_a.ispis()
 
djelatnik_b.ispis()
 
 
kupac_c.ispis()
 
 
 
 
# kupci=[]
# while True:
#     naziv=input('Unesite naziv kupca: ')
#     oib=input('Unesite oib kupca: ')
#     email=input('Unesite email kupca: ')
#     telefon=input('Unesite telefon kupca: ')
#     sjediste=input('Unesite sjediste kupca: ')
#     djelatnost=input('Unesite djelatnost kupca: ')
#     kupci.append(Kupac(naziv,oib,email,telefon,sjediste,djelatnost))

#     izlaz=input('Izlaz d/n: ')
#     if izlaz.lower()=='d':
#         break

# for kupac in kupci:
#     kupac.ispis()





djelatnici=[]
while True:
    ime=input('Unesite ime djelatnika: ')
    prezime=input('Unesite prezime djelatnika: ')
    oib=input('Unesite oib djelatnika: ')
    email=input('Unesite email djelatnika: ')
    telefon=input('Unesite telefon djelatnika: ')
    adresa=input('Unesite adresa djelatnika: ')
    radno_mjesto=input('Unesite radno mjesto djelatnika: ')
    djelatnici.append(Djelatnik(ime, prezime, oib, email, telefon, adresa, radno_mjesto))

    izlaz=input('Izlaz d/n: ')
    if izlaz.lower()=='d':
        break

for djelatnik in djelatnici:
    djelatnik.ispis()
class Osoba():
    def __init__(self):
        self.ime=''
        self.oib=''
        self.adresa='Split'

class Tvrtka(Osoba):
    def __init__(self):
        super().__init__()
        self.broj_djelatnika=25
        self.pravni_oblik='d.d.'

class Djelatnik(Osoba):
    def __init__(self):
        super().__init__()
        self.radno_mjesto='Prodavac'

osoba_a=Osoba()
tvrtka_b=Tvrtka()
print(tvrtka_b.broj_djelatnika)
djelatnik_c=Djelatnik()
print(djelatnik_c.radno_mjesto)

print(osoba_a.adresa)
print(tvrtka_b.adresa)
print(djelatnik_c.adresa)
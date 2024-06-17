class Osoba():
    def __init__(self, ime, oib, adresa):
        self.ime = ime
        self.oib = oib
        #self.ssn = oib
        self.adresa = adresa

class Tvrtka(Osoba):
    def __init__(self, ime, oib, adresa, broj_djelatnika, pravni_oblik):
        Osoba.__init__(self, ime, oib, adresa)
        self.broj_djelatnika=broj_djelatnika
        self.pravni_oblik=pravni_oblik

class Djelatnik(Osoba):
    def __init__(self, ime, oib, adresa, radno_mjesto):
        Osoba.__init__(self, ime, oib, adresa)
        self.radno_mjesto=radno_mjesto




osoba_a=Osoba('Mate',12345678901, 'Split')
print(osoba_a.ime, osoba_a.oib, osoba_a.adresa)

tvrtka_b=Tvrtka('MBO',19876543210, 'Zagreb',25,'d.d.')
print(tvrtka_b.ime, tvrtka_b.oib, tvrtka_b.adresa, tvrtka_b.broj_djelatnika, tvrtka_b.pravni_oblik)

djelatnik_c=Djelatnik('Jure', 4627219184739, 'Zadar', 'Prodavac')
print(djelatnik_c.ime, djelatnik_c.oib, djelatnik_c.adresa, djelatnik_c.radno_mjesto)
class Osoba():
    def __init__(self):
        self.ime=''
        self.oib=''
        self.adresa=''


mate=Osoba()
mate.ime='Mate'
mate.oib='12345678901'
mate.adresa='Split'



print(f'{mate.ime} s oib: {mate.oib} ima prebivaliste u {mate.adresa}')

# mate.mob='38591234567'
# print(f'Njegov mob je {mate.mob}')

# jure=Osoba()
# jure.ime='Jure'

# imenik=[mate, jure]
# for osoba in imenik:
#     print(f'{osoba.ime}: {osoba.mob}')

class Tvrtka():
    def __init__(self):
        self.ime=''
        self.oib=''
        self.adresa=''
        self.broj_djelatnika=0
        self.pravni_oblik=''

class Djelatnik():
    def __init__(self):
        self.ime=''
        self.oib=''
        self.adresa=''
        self.radno_mjesto=''
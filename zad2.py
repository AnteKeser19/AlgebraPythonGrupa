# class NazivKlase:
#     '''
#     Ovo nam sluzi za opis klase
#     '''
#     pass

# objekt1=NazivKlase()
# objekt2=NazivKlase()


# class TV():
#     '''Best tv in the world'''
#     dijagonala=55
#     proizvodjac='Sony'
#     model='S55X'
#     je_ukljucena=False

#     def ukljuci(self):
#         self.je_ukljucena=True

# tv_u_dnevnom=TV()

# print(f'Proizvodjac: {tv_u_dnevnom.proizvodjac}')
# print(f'Dijagonala: {tv_u_dnevnom.dijagonala}')
# print(f'Stanje TV: {tv_u_dnevnom.je_ukljucena}')
# tv_u_dnevnom.ukljuci()
# print(f'Stanje TV: {tv_u_dnevnom.je_ukljucena}')

# tv_u_sobi=TV()
# print(f'Proizvodjac: {tv_u_sobi.proizvodjac}')
# print(f'Dijagonala: {tv_u_sobi.dijagonala}')
# print(f'Stanje TV: {tv_u_sobi.je_ukljucena}')
# tv_u_sobi.ukljuci()
# print(f'Stanje TV: {tv_u_sobi.je_ukljucena}')


class TVNova():
    '''TV s konstruktorom'''
    def __init__(self, dijagonala, proizvodjac, model, program=0, glasnoca=0, je_ukljucen=False):
        self.dijagonala=dijagonala
        self.proizvodjac=proizvodjac
        self.model=model
        self.program=program
        self.glasnoca=glasnoca
        self.je_ukljucen=je_ukljucen

    def ukljuci(self):
        self.je_ukljucen=True
        self.program=1
        self.glasnoca=3
    
    def iskljuci(self):
        self.je_ukljucen=False
        self.program=0
        self.glasnoca=0

    def program_plus(self):
        self.program+=1
        if self.program==31:
            self.program=0

    def program_minus(self):
        self.program-=1
        if self.program==-1:
            self.program=30
        
    def program_broj(self, broj_programa):
        if broj_programa>=0 and broj_programa<=30:
            self.program=broj_programa

    def pojacavanje_glasnoce(self,broj=2):
        self.glasnoca+=broj
        if self.glasnoca>20:
            self.glasnoca=20

    def smanjivanje_glasnoce(self,broj=2):
        self.glasnoca-=broj
        if self.glasnoca<0:
            self.glasnoca=0
    
    def mute(self):
        self.glasnoca=0



novi_tv_dnevni=TVNova(72,'LG','L72XYZ')
novi_tv_soba=TVNova(32,'Samsung','S32Hype')

print(f'Dijagonala tv u dnevnom je {novi_tv_dnevni.dijagonala}')
print(f'Proizvodjac tv u sobi je {novi_tv_soba.proizvodjac}')

#dodati pojacavanje i smanjivanje zvuka (0-20), te mute botun (glasnoca=0)
#dodati metodu za gasenje
#primjeniti metode za paljenje, gasenje, promjenu programa, glasnocu i ispisati promjene u svakom koraku

print()
print(f'TV je ukljucen: {novi_tv_dnevni.je_ukljucen}')
print('Ukljuci TV!')
novi_tv_dnevni.ukljuci()
print(f'TV je ukljucen: {novi_tv_dnevni.je_ukljucen}')
print('Isljuci TV!')
novi_tv_dnevni.iskljuci()
print(f'TV je ukljucen: {novi_tv_dnevni.je_ukljucen}')

print()
novi_tv_dnevni.ukljuci()
print(f'TV je ukljucen na program: {novi_tv_dnevni.program}')
print('Prebaci na program 15.')
novi_tv_dnevni.program_broj(15)
print(f'TV je ukljucen na program: {novi_tv_dnevni.program}')

print()
print(f'Trenutna glasnoca je: {novi_tv_dnevni.glasnoca}')
print('Pojacaj glasnocu za 5.')
novi_tv_dnevni.pojacavanje_glasnoce(5)
print(f'Trenutna glasnoca je: {novi_tv_dnevni.glasnoca}')

print('Smanji glasnocu za 2.')
novi_tv_dnevni.smanjivanje_glasnoce(2)
print(f'Trenutna glasnoca je: {novi_tv_dnevni.glasnoca}')

print('Utisaj do kraja!')
novi_tv_dnevni.mute()
print(f'Trenutna glasnoca je: {novi_tv_dnevni.glasnoca}')

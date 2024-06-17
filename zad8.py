class Brojac():
    counter=0
 
    def __init__(self):
        Brojac.counter+=1
 
    def __del__(self):
        Brojac.counter-=1
 
 
    def stanje_countera(self):
        print(self.counter)
 
    @classmethod
    def stanje(cls):
        print(cls.counter)
 
    @classmethod
    def smanji(cls):
        cls.counter-=1
 
    @staticmethod
    def info():
        print('Informacije o ovoj klasi i objektima')
 
 
 
b1=Brojac()
b1.stanje_countera()
b2=Brojac()
b3=Brojac()
b4=Brojac()
b2.stanje_countera()
b1.stanje_countera()
Brojac.stanje()
b5=Brojac()
Brojac.stanje()
 
lista_brojaca=[]
for i in range(5):
    lista_brojaca.append(Brojac())
 
Brojac.stanje()
lista_brojaca.pop()
Brojac.stanje()
 
Brojac.info()
b1.info()

#generirati listu brojaca, s pop izbaciti brojac, prikazati koliko ih je
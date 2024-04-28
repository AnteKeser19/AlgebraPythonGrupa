def zbroji(a,b):
    try:
        zbroj =int(a)+int(b)
        return zbroj
    except:
        return 'Greska'
    
def dijeli(a,b=1):
    '''
    funkcija za dijeljenje s ciscenjem ulaznih vrijednosti
    '''
    try:  
        kvocijent = int(a)//int(b)
        return kvocijent
    except ZeroDivisionError:
        return 'Nije moguce dijeliti s nulom'

broj1 ='5' #input('Unesi broj 1: ')
broj2 ='3' #input('Unesi broj 2: ')
rezultat = zbroji(broj1,broj2)
# print(broj1+broj2)
print(rezultat)

print(dijeli(9,2))
print(dijeli(5))
print(dijeli(6,0))
print(dijeli('7','3'))

def iznos_pdv(osnovica:float):
    # pdv = osnovica*0.25
    return osnovica

cijena_bez_pdv = '100.0'
pedeve = iznos_pdv(cijena_bez_pdv)
iznos_pdva = iznos_pdv(cijena_bez_pdv)
ukupna_cijena = cijena_bez_pdv+iznos_pdva
print(cijena_bez_pdv,iznos_pdva,ukupna_cijena)

def ispisi_cijenu(neto, pdv=0.25, rabat=0):
    ukupno = neto*(1+pdv)*(1-rabat)
    print(f'Neto: {neto} + {neto*pdv} = {neto*(1+pdv)}\nRabat = {rabat*100}%\nUkupno={ukupno}')

ispisi_cijenu(100,0.25,0.2)

ispisi_cijenu(80,rabat=0.10)

ispisi_cijenu(rabat=0.2,pdv=0.1,neto=300)

# Prosli domaci , izvest ga koristeci funkcije zasebna funkcija meni, uplati ....
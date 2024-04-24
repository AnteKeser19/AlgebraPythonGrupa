import random

def baci_kockicu():
    return random.randint(1, 6)

def baci_kockice(broj_kockica, broj_bacanja):
    rezultati = []
    for _ in range(broj_bacanja):
        bacanje = [baci_kockicu() for _ in range(broj_kockica)] # malo vise obratiti paznju
        rezultati.append(bacanje)
    return rezultati

broj_kockica = int(input("Unesite broj kockica: "))
broj_bacanja = int(input("Unesite broj bacanja: "))

rezultati_bacanja = baci_kockice(broj_kockica, broj_bacanja)

for x, rezultat in enumerate(rezultati_bacanja,1):
    print(f"Bacanje {x}: {rezultat}")









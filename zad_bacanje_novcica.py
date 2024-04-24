# napravi igru u kojoj ce bacati novcic i ispisuje glava ili pismo
#prosiri tako da mozes bacati vise puta dok korisnik ne upise x za izlaz
#prosiri tako da glavni dio koda izvezes u funkciju bacanje_novcica() koja vraca trazeni broj

#napravi igru koja izbaciju kockicu koja ispisuje 1 do 6
#prosiri tako da mozes odbrati broj kockica koje se bacauju i broj bacanja
#prosiri tako da glavni dio koda izvezes u fukniciji baci:kockicu(broj_kocicka,broj_bacanja)
#koja vraca tupple ili listu sa nizom vrijednosti iz navedenih bacanja

import random

def bacanje_novcica():
    
    return random.choice(["Glava", "Pismo"])

def main():
    print("Dobrodošli u igru bacanja novčića!")
    while True:
        igrac = input("Pritisnite 'Enter' za bacanje novčića ili unesite 'x' za izlaz: ")
        
        if igrac.lower() == 'x':
            print("Hvala na igranju. Doviđenja!")
            break
        
        rezultat = bacanje_novcica()
        print("Novčić je pao na:", rezultat)
        print()  
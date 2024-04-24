#Emil
#za instalaciju keyboard u VS code
#1 dolje u terminalu sa ctrl+c izaci iz python koda
#2 upisati pip install keyboard
#alternativno
#unutar VS code stisnuti shift+ctrl+p
#otvorit ce se gore prozor, utpikati python create terminal i onda napraviti korak 1 i 2 


import random 
from time import sleep #spavanje u kodu
import keyboard 

#zadatak 1
# napravi igru u kojoj ces bacati novcic - ispisuje Glava ili Pismo
# prosiri tako da mozes bacati vise puta, dok korisnik ne unese x kao izlaz
# prosiri tako glavni dio koda izvezes u funkciju bacanje_novcica() koja vraća trazeni teks

#zadatak 2
# napravi igru u kojoj ces bacati kockicu - ispisuje 1 do 6
# prosiri tako da mozes odabrati broj kockica koje se bacaju i broj bacanja
# prosiri tako da glavni dio koda izvezes u funkciju baci_kockicu(broj_kockica, broj_bacanja)
# koja vraca tupple ili listu sa nizom vrijednosti iz navedenih bacanja


def bacanje_novcica() -> str:
    """
    vraća string "glava" ili "pismo"
    """
    list=["pismo","glava"]
    print(type(random.choice(list)))
    return random.choice(list)


def bacanje_kockica(br_kock: int) -> list:
    """
    uzima integer broja kockica
    vraća listu nasumičnih brojeva za broj kockica
    """
    brojevi=[]
    for _ in range (br_kock):
        brojevi.append(random.randint(1,6))
    return brojevi


#1 zadatak
while True:
    if keyboard.is_pressed("x"): #ako je pritisnut x u trenutku kada je linija na redu izvršava se kod unutar if funkcije
        #moze biti i pametnije odrađeno: ako je stisnut onda promijeni status iz True u False 
        print("STOP")
        break
    print(bacanje_novcica())
    sleep(0.5) #spava 0.5 sekundi nakon printa red iznad i onda kreće dalje

#2 zadatak
while True:
    br_bacanja=int(input("upisi broj bacanja:"))
    br_kocki=int(input("upiši koliko kockica zelis baciti: "))
    for i in range(br_bacanja):
        print(f"za {i+1}. bacanje dobio si: {bacanje_kockica(br_kocki)}")
    
    pon_bac=input("upiši n/ne ako zelis prestati sa igrom: ")
    if pon_bac=="n" or pon_bac=="ne":
        break



import random
 
mine=[]
prikaz_mina=[]
 
#9 -> mina
#-1 -> nije popunjeno zasad
def ispisi_2d_listu(stupaca,redaka,lista):
    naslovni_redak_slova=[chr(x) for x in range(65,65+stupaca)]
    print('\t',end='')
    for s in naslovni_redak_slova:
        print(s,'\t',end='')
    print()
    for r in range(redaka):
        print()
        print(r+1,'\t',end='')
        for s in range (stupaca):
            print(lista[r*stupaca+s],'\t',end='')
        print()
 
 
 
def generiraj_mine(stupaca=6, redaka=6, broj_mina=5):
    for _ in range(broj_mina):
        mine.append(9)
    for _ in range(stupaca*redaka-broj_mina):
        mine.append(-1)
    random.shuffle(mine)
 
def generiraj_broj_mina(stupaca,redaka):
    for indeks in range(stupaca*redaka):
        if mine[indeks]==9:
            pass
        else:
            test=generiraj_testove(stupaca,redaka,indeks)
            ntest=[indeks+x for x in test]
            #alternativa za ntest
            # alttest=[]
            # for x in test:
            #     alttest.append(indeks+x)
            broj_mina=0
            for t in ntest:
                if mine[t]==9:
                    broj_mina+=1
            mine[indeks]=broj_mina
 
 
 
        #prvi pokusaj
        # br_mina=0
        # if mine[indeks]==9:
        #     pass
        # elif indeks==0:
        #     if mine[indeks+1]==9:
        #         br_mina+=1
        #     if mine[indeks+stupaca]==9:
        #         br_mina+=1
        #     if mine[indeks+stupaca+1]==9:
        #         br_mina+=1
        #     mine[indeks]=br_mina
        # elif indeks==(stupaca-1):
        #     if mine[indeks-1]==9:
        #         br_mina+=1
        #     if mine[indeks+stupaca]==9:
        #         br_mina+=1
        #     if mine[indeks+stupaca-1]==9:
        #         br_mina+=1
        #     mine[indeks]=br_mina
 
        #     # to be contined...
 
 
def generiraj_testove(stupaca, redaka, indeks):
    uvjeti_testiranja={
        'UL':[1,stupaca,stupaca+1],
        'UR':[-1,stupaca,stupaca-1],
        'DL':[1,-stupaca,-stupaca+1],
        'DR':[-1,-stupaca,-stupaca-1],
        'L':[1,-stupaca,stupaca,-stupaca+1,stupaca+1],
        'R':[-1,-stupaca,stupaca,-stupaca-1,stupaca-1],
        'U':[-1,1,stupaca,stupaca-1,stupaca+1],
        'D':[-1,1,-stupaca,-stupaca-1,-stupaca+1],
        'O':[-1,1,-stupaca,stupaca,-stupaca-1,-stupaca+1,stupaca-1,stupaca+1]
    }
    if indeks==0:
        return uvjeti_testiranja['UL']
    elif indeks==(stupaca-1):
        return uvjeti_testiranja['UR']
    elif indeks==(stupaca*redaka-stupaca):
        return uvjeti_testiranja['DL']
    elif indeks==(stupaca*redaka-1):
        return uvjeti_testiranja['DR']
    elif indeks%stupaca==0:
        return uvjeti_testiranja['L']
    elif indeks%stupaca==(stupaca-1):
        return uvjeti_testiranja['R']
    elif indeks//stupaca==0:
        return uvjeti_testiranja['U']
    elif indeks//stupaca==(redaka-1):
        return uvjeti_testiranja['D']
    else:
        return uvjeti_testiranja['O']
 
 
#############
#0#1#2#3#4#5#
#6#7#8#9#10#11#
#12#13#14
 
def unesi_polje(stupaca, redaka):
    while True:
        zadnje_slovo=chr(65+stupaca-1)
        oznaka_polja=input(f'Unesi polje u obliku A1 do {zadnje_slovo}{redaka}: ').upper()
        slovo=oznaka_polja[0]
        odabrani_stupac=ord(slovo)-65 # npr. za A->65->0
        stupac_ok=True
        if odabrani_stupac<0 or odabrani_stupac>=stupaca:
            stupac_ok=False
        broj=oznaka_polja[1:]  #samo dvoznamenkasti brojevi
        try:
            odabrani_redak=int(broj)-1  #retci su oznaceni s 1 do n, ali indeksi idu od 0
            indeks_u_polju=odabrani_redak*stupaca+odabrani_stupac
            #print(indeks_u_polju)
        except:
            continue
        redak_ok=True
        if odabrani_redak<0 or odabrani_redak>=redaka:
            redak_ok=False
        if stupac_ok and redak_ok:
            if prikaz_mina[indeks_u_polju] != '[ ]': # Ova linija provjerva je li odabrano polje različito od '[ ]' , ukoliko je ispisat će da je polje već
                print('To polje je već otkriveno')
            else:
                return indeks_u_polju
        else:
            continue

# Otkrivanje polja "0' V1 23.4.'24 - 14:04 - Ante Keser
'''
Pokušajte modificirati kod, ako ima nešto nepotrebno izbacite
ako znate neki drugi način ili ako imate ideju da ovo riješite u manje linija koda
Moj dio (ln. 142 do ln. 173) zakomentirajte pa ubacite svoj kod i imenujte ga tipa V2 , V3 itd.
Tako da na predavanju možemo prikazati više raznih primjera.

'''  
 
def otkrij_prazna_polja(indeks, stupaca, redaka):
    '''
    Oktriva sva susjedna polja s brojem "0" (NISAM uspio napraviti da prikaže i polja s brojevima "1" "2" itd.)
    Odnosno polja koja prikazuju broj koliko je bombi u okolini.
    Ako netko ima ideju kako to implementirati - go for it.

    Ova funkcija prima argumente "indeks" njega prima iz razloga što je to index praznog polja kojeg funkcija otkriva
    te također prima broj stupaca i redaka.
    '''
    if prikaz_mina[indeks] != '[ ]' or mine[indeks] !=0:
        return
    prikaz_mina[indeks] = f'[{mine[indeks]}]'
    susjedna_polja = generiraj_testove(stupaca,redaka,indeks)
    for susjed in susjedna_polja:
        novi_indeks = indeks + susjed
        if 0 <= novi_indeks < stupaca*redaka:
            otkrij_prazna_polja(novi_indeks,stupaca,redaka)

def otkrij_polje(indeks):
    if mine[indeks] == 0: 
        otkrij_prazna_polja(indeks,stupaca,redaka)
    elif prikaz_mina[indeks] == '[ ]':
        if mine[indeks] == 9:
            prikaz_mina[indeks] ='[9]' # Kada sam modificirao kod, nakon što igrač "stane" na minu to polje se nije prikazalo, taj dio sam pokvario pa sam ga popravio na ovaj način - drukčiji nego originalni popravio. (ln. 152 i 153.)
        else:
            prikaz_mina[indeks]=f'[{mine[indeks]}]'
        if mine[indeks] == 0:
            otkrij_prazna_polja(indeks,stupaca,redaka)
    ispisi_2d_listu(stupaca,redaka,prikaz_mina) # Ovu funkciju pozivamo ponovno jer želimo ažurirati ploču igre
    if mine[indeks]== 9:
        return True, 'Bomba je eksplodirala!'
    return False, 'Nastavi dalje'

def igra_gotova():
    the_end=True
 
    for indeks in range(stupaca*redaka):
        if prikaz_mina[indeks]=='[ ]' and mine[indeks]!=9:
            the_end=False
    return the_end
 
def generiraj_prikaz_mina(stupaca, redaka):
    global prikaz_mina
    prikaz_mina=['[ ]' for _ in range(stupaca*redaka)]
 
 
 
 
 
while True:
 
    stupaca=6
    redaka=6
    broj_mina=5
    generiraj_mine(stupaca,redaka,broj_mina)  #polje mina popunjeno
    generiraj_prikaz_mina(stupaca,redaka)  #prazni prikaz mina
 
 
    #print(mine)
    #print(len(mine))
 
    generiraj_broj_mina(stupaca,redaka)  #popunjava brojke za okolinu mina
    #print(mine)
 
    # print()
    # print(generiraj_testove(stupaca,redaka,5))
 
    # print()
    # ispisi_2d_listu(stupaca,redaka,mine)
    # print()
    # print(prikaz_mina)
    # print()
    ispisi_2d_listu(stupaca,redaka,prikaz_mina)   #prikazuje na ekranu polje za igranje
    print()
 
    #########GLAVNI#########
    counter=0
    while True:
        counter+=1
        unos_po_indeksu=unesi_polje(stupaca,redaka)
        brzi_izlaz,tekst=otkrij_polje(unos_po_indeksu)
 
        gotovo=igra_gotova()
        if gotovo:
            tekst='Čestitamo, pobijedili ste!'
        print(tekst)
 
        if counter==50 or brzi_izlaz or gotovo:
            break
    print('Hvala na igranju')
 
    izlaz_iz_igre=input('Nastavi dalje d/n: ').lower()
    if izlaz_iz_igre=='n':
        break
 
 
# possible homework
 
# zad.1
# otkrivanje polja radi unosom npr. A1 do F6, 
# označavanje bombe napraviti unosom *A1 do *F6, s tim da
# ponovnim unosom istog polja se marker uklanja
# bombe označiti sa [B]
 
# zad.2
# automatsko otkrivanje polja ukoliko pogodimo polje oznake 0,
# sve do rubova s nekim brojem
 
# zad.3
# upozoriti ukoliko je neko polje vec otvoreno 
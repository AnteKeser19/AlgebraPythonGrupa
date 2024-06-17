import random
 
mine=[]
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
 
 
stupaca=6
redaka=6
broj_mina=5
generiraj_mine(stupaca,redaka,broj_mina)
 
print(mine)
print(len(mine))
 
generiraj_broj_mina(stupaca,redaka)
print(mine)
 
# print()
# print(generiraj_testove(stupaca,redaka,5))
 
print()
ispisi_2d_listu(stupaca,redaka,mine)
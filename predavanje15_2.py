import random
operatori=['+','-','*','/']
def slucajni_broj(min=0, max=100):
    return random.randint(min,max)
def slucajni_operator(operatori):
    return random.choice(operatori)
def level1():
    broj1=slucajni_broj()
    broj2=slucajni_broj()
    operator=slucajni_operator(operatori)
    zadatak=f'{broj1} {operator} {broj2} = '
    match operator:
        case '+':
            return broj1+broj2,zadatak
        case '-':
            return broj1-broj2,zadatak
        case '*':
            return broj1*broj2,zadatak
        case '/':
            if broj1==0 or broj2==0:
                return -100000000,zadatak
            rjesenje=slucajni_broj(0,10)
            broj2=slucajni_broj(1,10)
            broj1=rjesenje*broj2
            zadatak=f'{broj1} {operator} {broj2} = '
            return broj1//broj2,zadatak
level=1
broj_pitanja=20
trenutno_pitanje=0
ostvareni_bodovi=0
while level==1 and trenutno_pitanje<broj_pitanja:
    granice=[0,100]
    test=granice[0]-1
    while test<granice[0] or test>granice[1]:
        rjesenje,zadatak=level1()
        test=rjesenje
    #print(f'{zadatak}{rjesenje}') #nema smisla ako zadajemo zadatak, zakomentirati poslije
 
    while True:
        print(f'{zadatak}',end='')
        unos=input()
        if unos=='x':
            level=0
            break
        try:
            broj=int(unos)
            trenutno_pitanje+=1
        except:
            continue
        if broj==rjesenje:
            ostvareni_bodovi+=1
            print(f'Tocno! ({ostvareni_bodovi}/{trenutno_pitanje})')
 
        else:
            print(f'Netocno! ({ostvareni_bodovi}/{trenutno_pitanje})')
        print('x za izlaz')
        break
 

# izdvojiti dijelove koda u zasebne cijeline kroz funkcije
# trenutno se "zakopavamo" u nizu while petlji koje bi trebali nekako izbjeci (multilevel)
# prelazak na level2, 3, n rjesavanjem prethodnog levela u 20/20 varijanti
# korisnici - unosi svoje ime koje spremamo, i uz njega asociramo ostvarene bodove i level
# npr. Mate, 16, 2 (ime, bodovi, level)
# scoreBoard() - Izlistava najboljih troje ili n natjecatelja
# sto znaci l2, l3, koje operacije dopustit, kako napraviti da bude "rjesivo" 

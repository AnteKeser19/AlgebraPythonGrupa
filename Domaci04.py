#D.R. Napisati funkcije kao pomoc za racunanje udaljenosti tocaka od ishodista
# udaljenost(x, y, z=0) - prima 2 ili 3 parametra, racuna udaljenost od ishodista
# po forumuli (sqrt(x^2 + y^2 + z^2))
# vraca izracunato pomocu return pozivatelju
 
# napisi funkciju usporedi(tocka1,tocka2) koja prima tupple ili listu za tocku 1 i tocku2
# kao rezultat, racuna udaljnost t1 i t2 od ishodista pozivima funkcije udaljenost i ispisuje
# Tocka 3,4,2 je bliza ishodistu od tocke 5,11 (0 je implicitna)
#             je udaljenija od 
#             je jednako udaljena od 
 
#pozivi
#print(f'Tocka (3,4,5) je od ishodista udaljena {udaljenost(3,4,5)})
#t1=(3,2,5)
#t2=(6,29)
#ispis je Tocka 3,2,5 je bliza ishodistu od tocke 6,29
import math

def udaljenost(x,y,z=0):
    return math.sqrt(x**2 + y**2 + z**2)

def usporedba(tocka1, tocka2):
    udaljenost_tocke1 = udaljenost(*tocka1)
    udaljenost_tocke2 = udaljenost(*tocka2)
    udaljenost_tocke1 = round(udaljenost_tocke1, 2)
    udaljenost_tocke2 = round(udaljenost_tocke2, 2)

    print(f'Udaljenost Točke {tocka1} od ishodišta je: {udaljenost_tocke1}')
    print(f'Udaljenost Točke {tocka2} od ishodišta je: {udaljenost_tocke2}')

    if udaljenost_tocke1 < udaljenost_tocke2:
        print(f'Točka {tocka1} je bliža ishodištu od točke {tocka2}.')
    elif udaljenost_tocke1 > udaljenost_tocke2:
        print(f'Točka {tocka2} je bliža ishodištu od točke {tocka1}.')
    else:
        print(f'Točka {tocka1} i točka {tocka2} su jednako udaljene od ishodišta!')


# x1 = int(input('T1: kooridnata X: '))
# y1 = int(input('T1: kooridnata Y: '))
# z1 = int(input('T1: kooridnata Z: '))

# x2 = int(input('T2: kooridnata X: '))
# y2 = int(input('T2: kooridnata Y: '))
# z2 = int(input('T2: kooridnata Z: '))


# tocka1 = (x1,y1,z1)
# tocka2 = (x2,y2,z2)

tocka1 = (8,4,2)
tocka2 = (5,11,)


usporedba(tocka1, tocka2)

    
    
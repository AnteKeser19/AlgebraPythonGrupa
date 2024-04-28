lista=[3, 'Rijec', True, 3.14, [1,2,3], 'X']

print(lista[1])
print(lista[4])
print(lista[4][1])
print()
for element in lista:
    print(element)

for i in range (5):
    print(i,lista[i])

print()
for i in range (len(lista)):
    print(i,lista[i])

print()
#svi od 0 do 20 oboje ukljuceno

for i in range (21):
    print(i,end=', ')
print()
print()

#svi od 13 do 42 oboje ukljuceno

for i in range (13,43):
    print(i,end=', ')
print()
print()

#svako drugi broj od 13 do 42
for i in range (13,43,2):
    print(i,end=', ')
print()
print()

#parni od min do max
min = 13
max = 42
for i in range((min//2)*2+(min%2)*2, max+1, 2):
        print(i,end=', ')
print()
print()



min = 12
max = 42
for i in range((min//2)*2+1, max+1, 2):
        print(i,end=', ')
print()
print()

lista13_3 = []
for i in range (13, 27, 3):
    lista13_3.append(i)
    print(lista13_3)

print(list(range(13)))
lista_0_12 =list(range(13))
print(lista_0_12)

lista_13_3_new = list(range(13,27,3))
print(lista_13_3_new)

# u zadanom rasponu min i mix (ukljuceni), ispisi brojeve koji su djeljivi s "dijeljitelj"
print()
min = 14
max = 32
djeljitelj = 3
for i in range(min,max +1):
    if i % djeljitelj == 0:
         print(i)


# tablica mnozenja brojeva do 6
#     1 2 3 4 5 6
# 1   1 2 3 4 5 6
# 2   2 4 6 8 10 12
# 3
# 4
# 5
# 6
print()

redaka = 10
stupaca = 10
header_row =list(range(stupaca+1))
header_row[0]=''
for item in range (stupaca+1):
     print(header_row[item],end='\t')
print()
for redak in range(1,redaka+1):
    print()
    print(redak,end='\t')
    for stupac in range(1, stupaca+1):
         umnozak = redak*stupac
         print(umnozak,end='\t')
    print()

print()
print()

#ispiste SVE proste brojeve do max broja (max=72)
#26
# 26//2 = 13
#26%2=0 > nije prim broj
#7
#7 % 2= 1 > mozda je prim
# 7 % 3 = 1 >mozda je prim
#7% 4 = 3 > sigurno je prim
#15
#15 % 2 - 1 > mozda je prim
#15% 3 = 0 - sugrno nije prim


max_broj = 72
prim=True
for broj in range(3,max+1):
    prim=True
    for djeljitelj in range(2,(broj//2)):
         if broj % djeljitelj==0:
             prim=False
             print(f'Broj {broj} nije prim broj')
             break 
    
    if prim==True:
        continue
        print(f'Broj {broj} je prim broj')
   



  

# Broj u rasponu 1-10
# Broj X je paran / neparan

#Ispisi ukoliko je broj djeljiv s 3 ili s 5, osim ako je djeljiv s oba ta broja
#npr . 3 - djeljiv je s 3
#10 - djeljiv je s 5
#30 - ne smijem ga ispisati

broj = int(input('Upisi broj:'))

if broj % 2 == 0:
    print('Broj je paran!')
else:
    print('Broj je neparan')

if broj % 3 == 0 and broj % 5 == 0:
    pass
elif broj % 3 == 0:
    print('Broj je djeljiv s 3.')
elif broj % 5 == 0:
    print('Broj je djeljiv s 5')
else:
    print('Broj nije djeljiv ni s 3 ni s 5')

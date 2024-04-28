bodovi = 64
max_bodovi = 80

if bodovi < 40 and bodovi>=0:
    print('Niste polozili')
elif bodovi <50:
    print('Ocjena 2')
else:
    print('Polozili ste')

if bodovi <0:
    print('Krivi broj bodova')
elif bodovi<50:
    print('Ocjena 1')
elif bodovi <60:
    print('Ocjena 2')
elif bodovi <70:
    print('ocjena 3')
elif bodovi <80:
    print('Ocjena 4')
elif bodovi<=90:
    print('Ocjena 5')
else:
    print('Krivi broj bodova')




spol = 'm'
if spol =='m' or spol== 'M':
    print('Musko je!')
else:
    print('Zensko je')

zaposlen = True
if not zaposlen:
    print('Nije zaposlen')


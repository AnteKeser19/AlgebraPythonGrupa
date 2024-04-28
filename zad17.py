print()
# ulaz = input('Unesi broj: ')
broj = int('a',16)
print(broj)
'''
chr
ord
bin
oct
float
hex
'''
brojoct= oct(broj)

print(type(broj), type(brojoct))

print(type([1,2,3]))
print(type({1:'1',2:'2'}))
print(type((5,3)))
# print(type(5,3)) # no go

lista = [1,2,3]
slova = ['a','b','c']
print(slova[1])

rijec = 'aVIOn'
print(rijec)
print(rijec[2])
print(rijec.upper())
print(rijec.lower)

recenica = 'Danas je lijep i suncan dan, a sutra ce padati kisa'
rijeci = recenica.split(',')
print(rijeci)

rec2 = 'Sutra je cetvrtak'
rec2edit =rec2.replace('cetvrtak', 'petak')
print(rec2edit)
unos2 = '    ovo    je    super    stvar!'
unos2edit = unos2.strip()
unos2edit =unos2edit.replace('    ',' ')
print(unos2edit)
print(recenica,len(recenica))
print(len(slova))

ocjecne = [1,3,2,5,4,4,4,2,1,3,2,5]
nadji_br_petica = ocjecne.count(5)
print(nadji_br_petica)

dani_u_tjednu = {
    'mon':'pon',
    'tue':'uto',
    'wed':'sri',
    'thu':'cet',
    'fri':'pet',
    'sat':'sub',
    'sun':'ned',
}

print(dani_u_tjednu['tue'])

print(list(dani_u_tjednu.keys())[2])

print(list(dani_u_tjednu.values())[2])

print(list(dani_u_tjednu.items())[2][1])

for ocjena in ocjecne:
    print(ocjena,end=' ')
print()
print('Hvala na koristenju')

for key in dani_u_tjednu.keys():
    print(key,dani_u_tjednu[key])

for value in dani_u_tjednu.values():
    print(value)

for both in dani_u_tjednu.items():
    key, value = both
    print(key, value)

for key, value in dani_u_tjednu.items():
    print(key,value)

dani = [(1,'Pon','Ponedjeljak'),(2,'uto','Utorak'),(3,'sri','Srijeda')]

for dan in dani:
    redni, kratica, puni_naziv = dan
    print(dan)
    print(f'{redni}. dan u tjednu je {puni_naziv}, skraceno {kratica}')

for redni, kratica, puni_naziv in dani:
    print(f'{redni}. dan u tjednu je {puni_naziv}, skraceno {kratica}')
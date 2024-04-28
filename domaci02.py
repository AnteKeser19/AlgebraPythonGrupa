# Unesi broj1: 2
# Unesi broj2: 7
# unesi operator:+(+,-,*,/,**,//,%)

# Unesi niz od 10 brojeva. Ukoliko je uneseni broj < 0, izidji i zbroji samo postojece brojeve
# inace zbroji svih 10 brojeva

# Koristeci for petlju, conttinue i break, ispisi sve brojeve do 100 osim onih djeljivih sa 7,
# a kada dodjes do broja 83 izidji iz petlje


prvi_broj = int(input('Unesite prvi broj: '))
drugi_broj = int(input('Unesite drugi broj: '))
operator = input('Unesite operator')

if operator == '+':
    print('Rezultat:',prvi_broj + drugi_broj)
elif operator == '-':
    print('Rezultat:',prvi_broj - drugi_broj)
elif operator == '*':
    print('Rezultat:',prvi_broj * drugi_broj)
elif operator == '/':
    print('Rezultat: ',prvi_broj / drugi_broj)
elif operator == '**':
    print('Rezultat: ',prvi_broj ** drugi_broj)
elif operator == '//':
    print('Rezultat: ',prvi_broj // drugi_broj)
elif operator == '%':
    print ('Rezultat: ',prvi_broj % drugi_broj)
else:
    print('Nevazeci operator!!')

brojevi1_10 = []

for i in range(10):
    broj = int(input(f'Unesite {i+1} broj: '))
    if broj < 0:
        break
    else:
        brojevi1_10.append(broj)

zbroj = sum(brojevi1_10)
print ('Zbroj unesenih brojeva je: ',zbroj)


for broj in range(1,101):
    if broj % 7 == 0:
        continue
    print(broj)
    if broj == 83:
        break
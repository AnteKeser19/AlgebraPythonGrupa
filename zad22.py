def meni():
    print('1. Zbroj')
    print('2. Razlika')
    print('0. Izlaz')

def obrada_unosa():
    unos = input('Unesi broj: ')
    return unos



def unesi_dva_broja():
    while True:
        b1 = input('Unesi prvi broj: ')
        if b1.isnumeric():
            b1 = int(b1)
            break
    while True:
        b2 = input('Unesi drugi broj: ')
        if b2.isnumeric():
            b2 = int(b2)
            break
    return b1,b2


def zbroji():
    # print('Zbrajam')
    b1,b2 = unesi_dva_broja()
    return b1+b2
def oduzmi():
    # print('Oduzimam')
    b1,b2 = unesi_dva_broja()
    return b1-b2


def selektor(unos):
    if unos == '1':
        print('Zbroj')
        print(zbroji())
    elif unos == '2':
        print('Razlika')
        print(oduzmi())
    else:
        print('Krivi unos')



while True:
    meni()
    unos = obrada_unosa()
    if unos == '0' or unos.lower() == 'x':
        break
    selektor(unos)

print('Hvala na koristenju')



broj = 1
# broj = '0'
#brojint = int(broj)
# print(broj.isdigit())
# print(broj.isnumeric())
print(isinstance(broj,float))
#print(brojint)
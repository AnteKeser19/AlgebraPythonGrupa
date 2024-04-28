broj = 0

def povecajv1():
    global broj
    broj+=1
    print(f'Broj je sada {broj}')
    return (broj)

def povecajv2():
    global broj
    broj += 1 
    print(f'Broj je sada {broj}')
    return broj

def povecajv3():
    global broj
    broj += 1 
    print(f'Broj je sada {broj}')
    return broj

def povecajv4(broj):
    broj +=1
    print(f'Broj je sada {broj}')
    return broj




print(f'Broj je {broj}')
povecajv1()
povecajv2()
povecajv3()
povecajv4(broj)

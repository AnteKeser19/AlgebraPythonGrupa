b1 = 5
b2 = 7

def ispisi():
    print(f'Brojka 1 je {b1}')
    print(f'Brojka 2 je {b2}')

def promijenjene_brojke():
    b1 = 10
    b2 = 14
    print(f'Brojka 1 je {b1}')
    print(f'Brojka 2 je {b2}')   

def globalna_izmjena():
    global b1
    global b2
    b1 = 15
    b2 = 21
    print(f'Brojka 1 je {b1}')
    print(f'Brojka 2 je {b2}')   

def vrati4x():
    b1 = 5
    b2 = 7
    print(f'Brojka 1 je {4*b1}')
    print(f'Brojka 2 je {4*b2}')
    return (4*b1,4*b2)

def podijelis4(b1,b2):
    b1//= 4
    b2//= 4
    print(f'Brojka 1 je {b1}')
    print(f'Brojka 2 je {b2}')
    return b1,b2

print(f'Glavni: Brojka 1 je {b1}')
print(f'Glavni: Brojka 2 je {b2}')
ispisi()
print(f'Glavni: Brojka 1 je {b1}')
print(f'Glavni: Brojka 2 je {b2}')
promijenjene_brojke()
print(f'Glavni: Brojka 1 je {b1}')
print(f'Glavni: Brojka 2 je {b2}')
globalna_izmjena()
print(f'Glavni: Brojka 1 je {b1}')
print(f'Glavni: Brojka 2 je {b2}')
b1,b2 = vrati4x()
print(f'Glavni: Brojka 1 je {b1}')
print(f'Glavni: Brojka 2 je {b2}')
b1,b2 = podijelis4(b1,b2)
print(f'Glavni: Brojka 1 je {b1}')
print(f'Glavni: Brojka 2 je {b2}')

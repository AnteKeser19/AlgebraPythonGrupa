import random

def pocetak_programa():
    print('Dobrodošli u MathSolver!')
    input('Unesite vaše ime: ')
    meni()

def unos_broja(prompt):
    while True:
        unos = input(prompt)
        if unos.isdigit():
            return int(unos)
        else:
            print('Molimo unesite cijeli broj!')

def zbrajanje():
    bodovi = 0
    for _ in range(6):
        broj1 = random.randint(1, 10)
        broj2 = random.randint(1, 10)
        odgovor = unos_broja(f"Koliko je {broj1} + {broj2}? ")
        if broj1 + broj2 == odgovor:
            bodovi += 1
            print("Točno!")
        else:
            print("Netočno!")
    return bodovi

def oduzimanje():
    bodovi = 0
    for _ in range(6):
        broj1 = random.randint(1, 10)
        broj2 = random.randint(1, broj1)
        odgovor = unos_broja(f"Koliko je {broj1} - {broj2}? ")
        if broj1 - broj2 == odgovor:
            bodovi += 1
            print("Točno!")
        else:
            print("Netočno!")
    return bodovi

def mnozenje():
    bodovi = 0
    for _ in range(20):
        broj1 = random.randint(1, 10)
        broj2 = random.randint(1, 10)
        odgovor = unos_broja(f"Koliko je {broj1} * {broj2}? ")
        if broj1 * broj2 == odgovor:
            bodovi += 1
            print("Točno!")
        else:
            print("Netočno!")
    return bodovi

def dijeljenje():
    bodovi = 0
    for _ in range(20):
        broj1 = random.randint(1, 10)
        broj2 = random.randint(1, 10)
        broj1, broj2 = max(broj1, broj2), min(broj1, broj2)
        while broj1 % broj2 != 0:
            broj1 = random.randint(1, 10)
            broj2 = random.randint(1, 10)
            broj1, broj2 = max(broj1, broj2), min(broj1, broj2)
        odgovor = unos_broja(f"Koliko je {broj1} / {broj2}? ")
        if broj1 / broj2 == odgovor:
            bodovi += 1
            print("Točno!")
        else:
            print("Netočno!")
    return bodovi


def meni():
    bodovi = 0
    while True:
        print("Odaberite razinu:")
        print("1. Zbrajanje")
        print("2. Oduzimanje")
        print("3. Množenje")
        print("4. Dijeljenje")
        print("5. Izlaz")
        
        odabir = input("Vaš odabir (1-5): ")
        
        if odabir == "1":
            bodovi += zbrajanje()
            print("Na kraju zbrajanja imate", bodovi, "bodova.")
        elif odabir == "2":
            if bodovi < 5:
                print('Nemate dovoljno bodova za pristup ovoj razini')
                meni()
            else:
                bodovi += oduzimanje()
                print("Na kraju oduzimanja imate", bodovi, "bodova.")
        elif odabir == "3":
            if bodovi < 10:
                print('Nemate dovoljno bodova za pristup ovoj razini')
                meni()
            else:
                bodovi += mnozenje()
                print("Na kraju množenja imate", bodovi, "bodova.")
        elif odabir == "4":
            if bodovi < 15:
                print('Nemate dovoljno bodova za pristup ovoj razini')
                meni()
            else:
                bodovi += dijeljenje()
                print("Na kraju dijeljenja imate", bodovi, "bodova.")
        elif odabir == "5":
            print("Hvala na igranju!")
            break
        else:
            print("Pogrešan unos. Molimo unesite broj od 1 do 5.")

pocetak_programa()
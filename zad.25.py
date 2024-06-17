import random

def bacanje_novcica():
    return random.choice ({'Glava', 'Pismo'})

def ispisi_scoreborad():
    for key, value in scoreboard.items():
        print(f'{key}\t{value}')


scoreboard={}

while True:
    ispisi_scoreborad()


    korisnik=input('Unesi svoj korisničko ime, (x za izlaz): ')
    if korisnik == 'x':
            break
    if 'korisnik' in scoreboard.keys():
        print(f'{korisnik} je u scoreboradu')
    else:
        print(f'{korisnik} nije u scrobradu. ali je odan')
        scoreboard[korisnik]=0

    suma=0
    glave=0
    while True:
        x=input('Stisni enter za bacanje novčića, x za izlaz')
        if x== 'x':
            break
        rezultat=bacanje_novcica()
        print('Rezulatat bacanja novčića: ',rezultat )
        suma+=1
        if rezultat== 'Glave':
            glave+=1
        omjer=round((glave/suma)*100,0)
        if scoreboard[korisnik]>omjer:
            scoreboard[korisnik]= omjer



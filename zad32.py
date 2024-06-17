import os
 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # u c/c++ (os.name=='nt')?os.system('cls'):os.system('clear')
    '''
    if os.name=='nt':
        os.system('cls')
    elif os.name=='clear':
        os.system('clear')
    '''
 
clear()
# py-dnevnik (pandan e-dnevnik)
##### KORISNICI ######
# user admin, password admin ima SVA prava, hardcoded u program, ima svojstva
# username: admin, password: admin, level: admin, razredi: citava_lista_svih_razreda
# ostali useri trebaju imati jedinstven username, password, level: razrednik ili nastavnik.
# ako je user razrednik samo PRVI razred u listi je taj kojem je razrednik i za koji ima dodatna prava
# za ostale razrede, ima prava kao i nastavnik, samo vidi svoj predmet
# korisnik moze biti i ucenik, s tim da on moze vidjeti samo svoje predmete i svoje ocjene
# ucenik moze bit pripradnik samo jednog razreda
 
svi_razredi=[]
razine_pristupa=['admin','razrednik','nastavnik','ucenik']
users={'admin':['admin', 'admin', svi_razredi]} # username: [password, level, lista_razreda]
 
 
 
 
 
 
##### PREDMETI #####
# predmeti imaju svoj jedinstveni ID predmeta npr. 1AMAT, 1AFIZ, 1AHRV, 1AENG, 1AXYZ
# ID je odredjen kao godina_razreda|slovo_razreda|troslovna_uppercase_oznaka_predmeta
# uz id je vezano polje informacija poput: Puni naziv predmeta, Nastavnik (user)
 
##### OCJENE #####
# sve ocjene se zapisuju u jedinstvenu listu ocjena, za citavi py-dnevnik
# svaka ocjena je predstavljena vlastitom listom ili dictionaryjem
# osim same brojcane ocjene, sastoji se i od ostalih informacija poput ID predmeta, ID ucenika, datum ocjene
# mogu se dodati i druge informacije vezane uz ocjenu cime se moze olaksati filtriranje i prikaz rezultata
 
##### MENIJI #####
# LOGIN - Unos username/password
# ADMIN MENI (dodavanje i uklanjanje korisnika, predmeta i ocjena po zelji, prikaz svih razreda, ocjena, korisnika)
# RAZREDNIK MENI (dodavanje i uklanjanje ocjena svog predmeta po zelji, prikaz svih ocjena u vlastitom razredu, 
# prikaz ocjena predmeta u drugim razredima kojima razrednik u ulozi nastavnika predaje)
# NASTAVNIK MENI (dodavanje i uklanjanje ocjena svog predmeta po zelji, prikaz ocjena predmeta u razredima kojima predaje)
# UCENIK MENI (prikaz ocjena svih predmeta koje ucenik pohadja)
 
 
start_meni=['Izlaz','Login']
admin_meni=['Logout','Korisnici','Razredi','Predmeti','Ocjene']
korisnici_meni=['Povrat','Prikazi korisnike','Dodaj korisnika','Ukloni korisnika']
razredi_meni=['Povrat','Prikazi razrede','Dodaj razred','Ukloni razred']
predmeti_meni=['Povrat','Prikazi predmete','Dodaj predmet','Ukloni predmet']
ocjene_meni=['Povrat','Prikazi ocjene','Upisi ocjenu','Izbrisi ocjenu']
 
def meni(meni_lista):
    #print(meni_lista)
    print('*'*20,'M E N I','*'*20)
    for rb,stavka in enumerate(meni_lista):
        print(f'\t\t{rb}. {stavka}')
 
    # print()
    # for stavka in meni_lista: #ver2.
    #     print(f'{stavka}')
 
    # for rb in range(len(meni_lista)): #ver3.
    #     print(f'{rb}')
 
    # for rb in range(len(meni_lista)): #ver4.
    #     print(f'{rb}. {meni_lista[rb]}')
 
 
def unesi_opciju(meni_lista):
    max_opcija=len(meni_lista)-1
    while True:
        try:
            opcija=int(input(f'Unesi opciju od 0 do {max_opcija}: '))
        except:
            print(f'Krivi unos!')
            continue
        if opcija>=0 and opcija<=max_opcija:
            return opcija
 
def unesi_login(entered_level='ucenik', change=False):
    min_username_length=1
    min_password_length=4
    while True:
        entered_username=input(f'Unesi korisnicko ime: ')
        entered_password=input(f'Unesi lozinku: ')
        if change:
            entered_level=input(f'Unesi razinu pristupa: {razine_pristupa}: ')
            if entered_level not in razine_pristupa:
                continue
        if len(entered_username)<min_username_length or len(entered_password)<min_password_length:
            continue
        return (entered_username,entered_password,entered_level)
 
 
def provjeri_korisnika(username,password,level):
    if username not in users.keys():
        print(f'{username} nije registrirani korisnik!')
        return False
    user_data=users[username]
    #print(user_data)
    stored_password, stored_level, stored_classes = user_data
    #print(stored_password, stored_level, stored_classes)
    check_password=False
    check_level=False
    if password==stored_password:
        check_password=True
    if level==stored_level:
        check_level=True
    return (check_password,check_level)
 
#admin sucelje i funkcije
def admin_sucelje():
    print('u admin sucelju smo')
    while True:
        clear()
        meni(admin_meni)
        opcija=unesi_opciju(admin_meni)
        if opcija==0:
            break
 
def razrednik_sucelje():
    print('u razrednik sucelju smo')
 
 
def nastavnik_sucelje():
    print('u nastavnik sucelju smo')
 
def ucenik_sucelje():
    print('u ucenik sucelju smo')
 
while True:
    clear()
    meni(start_meni)
    opcija=unesi_opciju(start_meni)
    if opcija==0:
        break
    else:
        #print(unesi_login(entered_level='admin'))
        username,password,level=unesi_login(entered_level='admin')
        #print(f'User: {username}\nPassword: {password}\nLevel: {level}')
 
    check_password, check_level = provjeri_korisnika(username,password,level)
    #print(check_password,check_level)
    check_ok=check_password #and check_level #ukljuciti ako ne zelimo da logiramo s drugim levelom 
    if not check_ok:
        continue
    match(level):
        case 'admin':
            admin_sucelje()
        case 'razrednik':
            razrednik_sucelje()
        case 'nastavnik':
            nastavnik_sucelje()
        case 'ucenik':
            ucenik_sucelje()
 
 
 
 
 
    print('natrag u glavnoj petlji')
    input()
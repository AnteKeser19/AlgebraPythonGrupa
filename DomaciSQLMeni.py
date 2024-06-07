import sqlite3
import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def MainMeni():
    create_table_query = '''CREATE TABLE IF NOT EXISTS Korisnici (
                         id INTEGER PRIMARY KEY, 
                         name TEXT NOT NULL,
                         surname TEXT NOT NULL,
                         passkey TEXT NOT NULL UNIQUE,
                         email TEXT NOT NULL UNIQUE,
                         br_tel INTEGER NOT NULL UNIQUE,
                         razina TEXT NOT NULL);'''
    
    database_name = 'LoginPodaci.db'

    try:
        sc = sqlite3.connect(database_name)
        cursor = sc.cursor()
        cursor.execute(create_table_query)
        sc.commit()
        cursor.close()
    except sqlite3.Error as e:
        print('Pogreška kod spajanja na bazu',e)
    finally:
        if sc: 
            sc.close()

    insert_into_table_query='''INSERT INTO Korisnici (name,surname, passkey ,email,br_tel,razina)
                            VALUES (?, ?, ?, ?, ?, ?)'''
    select_query ='''SELECT * FROM Korisnici WHERE email=?'''
 
    database_name='LoginPodaci.db'
    info = ('admin','admin','admin','admin',1,'admin')

    loginKorisnici = [
        info

    ]
 
    try:
        sc=sqlite3.connect(database_name)
        cursor=sc.cursor()
        for korisnik in loginKorisnici:
            cursor.execute(select_query,(korisnik[3],))
            postoji = cursor.fetchone()
            if postoji:
                pass
            else:
                cursor.execute(insert_into_table_query,korisnik)
        sc.commit()
        cursor.close()
    except sqlite3.Error as e:
        print('Pogreska kod spajanja na bazu',e)
    finally:
        if sc:
            sc.close()
    print('Dobrodošli u jednostavan PY-Login sustav!')
    print('1. Pristupi Login-u')
    print('2. Upravljaj Računima')
    print('0. Izlaz')
    while True:
        odabir = input('Odaberite željenu opciju: ')
        if odabir == '1':
            clear()
            Login_Menu()
            break
        elif odabir == '2':
            clear()
            Admin_Login()
            break
        elif odabir == '0':
            clear()
            print('Hvala na korištenju!')
            break
        else:
            print('Neispravan unos!')
            continue


def Admin_Login():
    while True:
        email = input('Unesite vaš email: ')
        passkey = input('Unesite vašu lozinku: ')
        razina = 'admin'
        login_table_query = '''SELECT passkey, razina FROM Korisnici WHERE email=?'''
        database_name = 'LoginPodaci.db'
        sc = sqlite3.connect(database_name)
        cursor = sc.cursor()
        cursor.execute(login_table_query,(email,))
        login = cursor.fetchone()
        sc.close()
        if login and login[0] == passkey and login[1] == razina:
            clear()
            Acc_Managment()
            break
        else:
            print('Nemate ovlasti!')
            continue

    
def Login_Menu():
    while True:
        email = input('Unesite vaš email: ')
        passkey = input('Unesite vašu lozinku: ')
        razina_K = 'korisnik'
        razina_A = 'admin'
        login_table_query = '''SELECT passkey, razina FROM Korisnici WHERE email=?'''
        database_name = 'LoginPodaci.db'
        sc = sqlite3.connect(database_name)
        cursor = sc.cursor()
        cursor.execute(login_table_query,(email,))
        login = cursor.fetchone()
        sc.close()

        check_who = '''SELECT * FROM Korisnici WHERE email=?'''
        database_name = 'LoginPodaci.db'
        sc = sqlite3.connect(database_name)
        cursor = sc.cursor()
        cursor.execute(check_who,(email,))
        cw = cursor.fetchall()
        sc.close()
        if login and login[0] == passkey and (login[1] == razina_A or login[1] == razina_K):
            clear()
            for user in cw:
                print(f'Prijavljeni ste kao: {user[6]} {user[1]} {user[2]}   ')
            sustav()
            break
        else:
            print('Neispravan email ili lozinka!')
            continue


def sustav():

    print('Uspješno ste prijavljeni')

def Acc_Managment():
    print('1. Stvori novi račun')
    print('2. Prikaži sve račune')
    print('3. Ažuriraj podatke računa')
    print('4. Ukloni račun')
    print('0. Izlaz')
    while True:
        odabir = input('Odaberite željenu opciju: ')
        if odabir == '1':
            clear()
            kreiraj_racun()
            break
        elif odabir == '2':
            clear()
            prikazi_racune()
            break
        elif odabir == '3':
            clear()
            update_racun()
            break
        elif odabir == '4':
            clear()
            delete_racun()
            break
        elif odabir == '0':
            clear()
            print('Hvala na korištenju!')
            break
        else:
            clear()
            print('Neispravan unos!')
            continue

def kreiraj_racun():
    while True:
        ime = input('Unesite ime: ')
        prezime = input('Unesite prezime: ')
        passkey = input('Unesite jedinstvenu lozinku: ')
        email = input('Unesite email korisnika: ')
        try:
            br_tel = int(input('Unesite broj telefona korisnika: '))
        except:
            print('Neispravan unos!')
            continue
        razina = input('Unesi razinu korisnika (admin ili korisnik): ')
        break
    info = (ime,prezime,passkey,email,br_tel,razina)

    insert_into_table_query='''INSERT INTO Korisnici (name,surname, passkey ,email,br_tel,razina)
                            VALUES (?, ?, ?, ?, ?, ?)'''
 
    database_name='LoginPodaci.db'
 
    loginKorisnici = [
        info

    ]
 
    try:
        sc=sqlite3.connect(database_name)
        cursor=sc.cursor()
        for korisnik in loginKorisnici:
            cursor.execute(insert_into_table_query,korisnik)
        sc.commit()
        cursor.close()
    except sqlite3.Error as e:
        print('Pogreska kod spajanja na bazu',e)
    finally:
        if sc:
            sc.close()
    clear()
    Acc_Managment()

def prikazi_racune():
    print('1. Prikaži sve račune')
    print('2. Prikaži određeni račun/e')
    while True:
        odabir = input('Odaberite željenu opciju: ')
        if odabir == '1':
            clear()
            show_all()
            break
        elif odabir == '2':
            clear()
            show_acc()
            break
        else:
            print('Neispravan unos!')
            continue

def show_all():
    select_table_query = '''SELECT * FROM Korisnici'''

    database_name = 'LoginPodaci.db'

    try:
        sc = sqlite3.connect(database_name)
        cursor = sc.cursor()
        cursor.execute(select_table_query)
        records = cursor.fetchall()
        for record in records:
            print(f'Ime: {record[1]} - Prezime: {record[2]} - Passkey: {record[3]} - Email: {record[4]} - Broj Telefona: {record[5]} - Razina: {record[6]}')
        cursor.close()
    except sqlite3.Error as e:
        print('Pogreška kod spajanja na bazu',e)
    finally:
        if sc: 
            sc.close()
    go_back = input('Za povratak na Upravljanje računima pritsite tipku Enter ')
    clear()
    Acc_Managment()

def show_acc():
    print('1. Prikaži račun prema id-u')
    print('2. Prikaži račun/e prema imenu')
    print('3. Prikaži račun/e prema prezimenu')
    while True:
        odabir = input('Odaberite željenu opciju: ')
        if odabir == '1':
            show_by_id()
            break
        elif odabir == '2':
            show_by_name()
            break
        elif odabir == '3':
            show_by_surname()
            break
        else:
            print('Neispravan unos!')
            continue

def show_by_id():
   print('1. Prikaži korisnika po id-u')
   print('2. Prikaži SVE korisnika iznad određenog id-a')
   while True:
        odabir = input('Odaberite željenu opciju: ')
        if odabir == '1':
            show_single_id()
            break
        elif odabir == '2':
            show_higher_id()
            break
        else:
            print('Neispravan unos!')
            continue

def show_single_id():
    id = input('Unesite ID tražene osobe: ')
    select_table_query = '''SELECT * FROM Korisnici WHERE id=?'''
    database_name = 'LoginPodaci.db'

    try:
        sc = sqlite3.connect(database_name)
        cursor = sc.cursor()
        cursor.execute(select_table_query,(id,))
        records = cursor.fetchall()
        for record in records:
            print(f'Ime: {record[1]} - Prezime: {record[2]} - Passkey: {record[3]} - Email: {record[4]} - Broj Telefona: {record[5]} - Razina: {record[6]}')
        cursor.close()
    except sqlite3.Error as e:
        print('Pogreška kod spajanja na bazu')
    finally:
        if sc: 
            sc.close()
    go_back = input('Za povratak na Upravljanje računima pritsite tipku Enter ')
    clear()
    Acc_Managment()

def show_higher_id():
    id = input('Unesite ID za koji će vam se prikazati svi korisnici s većim ID-em: ')
    select_table_query = '''SELECT * FROM Korisnici WHERE id>?'''
    database_name = 'LoginPodaci.db'

    try:
        sc = sqlite3.connect(database_name)
        cursor = sc.cursor()
        cursor.execute(select_table_query,(id,))
        records = cursor.fetchall()
        for record in records:
            print(f'Ime: {record[1]} - Prezime: {record[2]} - Passkey: {record[3]} - Email: {record[4]} - Broj Telefona: {record[5]} - Razina: {record[6]}')
        cursor.close()
    except sqlite3.Error as e:
        print('Pogreška kod spajanja na bazu')
    finally:
        if sc: 
            sc.close()
    go_back = input('Za povratak na Upravljanje računima pritsite tipku Enter ')
    clear()
    Acc_Managment()



def show_by_name():
    ime = input('Unesite ime korisnika kojeg/e želite prikazati: ')
    select_table_query = '''SELECT * FROM Korisnici WHERE name=?'''
    database_name = 'LoginPodaci.db'

    try:
        sc = sqlite3.connect(database_name)
        cursor = sc.cursor()
        cursor.execute(select_table_query,(ime,))
        records = cursor.fetchall()
        for record in records:
            print(f'Ime: {record[1]} - Prezime: {record[2]} - Passkey: {record[3]} - Email: {record[4]} - Broj Telefona: {record[5]} - Razina: {record[6]}')
        cursor.close()
    except sqlite3.Error as e:
        print('Pogreška kod spajanja na bazu')
    finally:
        if sc: 
            sc.close()
    go_back = input('Za povratak na Upravljanje računima pritsite tipku Enter ')
    clear()
    Acc_Managment()

def show_by_surname():
    prezime = input('Unesite prezime korisnika kojeg/e želite prikazati: ')
    select_table_query = '''SELECT * FROM Korisnici WHERE surname=?'''
    database_name = 'LoginPodaci.db'

    try:
        sc = sqlite3.connect(database_name)
        cursor = sc.cursor()
        cursor.execute(select_table_query,(prezime,))
        records = cursor.fetchall()
        for record in records:
            print(f'Ime: {record[1]} - Prezime: {record[2]} - Passkey: {record[3]} - Email: {record[4]} - Broj Telefona: {record[5]} - Razina: {record[6]}')
        cursor.close()
    except sqlite3.Error as e:
        print('Pogreška kod spajanja na bazu')
    finally:
        if sc: 
            sc.close()
    go_back = input('Za povratak na Upravljanje računima pritsite tipku Enter ')
    clear()
    Acc_Managment()

def update_racun():
    print('1. Ime')
    print('2. Prezime')
    print('3. Passkey')
    print('4. Email')
    print('5. Broj telefona')
    while True:
        odabir = input('Što želite ažurirati?: ')
        if odabir == '1':
            update(podatak='name')
            break
        elif odabir == '2':
            update(podatak='surname')
            break
        elif odabir == '3':
            update(podatak='passkey')
            break
        elif odabir == '4':
            update(podatak='email')
            break
        elif odabir == '5':
            update(podatak='br_tel')
            break
        else:
            print('Neispravan unos!')
            continue


def update(podatak):
    id = input(f'Unesite id korisnika čiji {podatak} želite ažurirati: ')
    select_table_query = '''SELECT * FROM Korisnici WHERE id=?'''
    database_name = 'LoginPodaci.db'

    try:
        sc = sqlite3.connect(database_name)
        cursor = sc.cursor()
        cursor.execute(select_table_query, (id,))
        records = cursor.fetchall()
        for record in records:
            print(f'Ime: {record[1]} - Prezime: {record[2]} - {record[3 if podatak == "passkey" else (4 if podatak == "email" else 5)]}')
        cursor.close()
    except sqlite3.Error as e:
        print('Pogreška kod spajanja na bazu', e)
    finally:
        if sc:
            sc.close()

    if podatak == 'br_tel':
        while True:
            try:
                nova_vrijednost = int(input(f'Unesite ažurirani {podatak} korisnika: '))
                break
            except:
                print('Neispravan unos!')
                continue
    else:
        nova_vrijednost = input(f'Unestie ažurirani {podatak} korisnika: ')

    update_table_query = f'''UPDATE Korisnici
                             SET {podatak} = ?
                             WHERE ID = ?'''      

    try:
        sc = sqlite3.connect(database_name)
        cursor = sc.cursor()
        cursor.execute(update_table_query, (nova_vrijednost, id))
        sc.commit()
        cursor.close()
    except sqlite3.Error as e:
        print('Pogreška kod spajanja na bazu', e)
    finally:
        if sc:
            sc.close()

    print(f'{podatak.capitalize()} korisnika je ažuriran')
    input('Za povratak na Upravljanje računima pritisnite tipku Enter ')
    clear()
    Acc_Managment()



# def update_name():
#     id = input('Unesite id korisnika čije ime želite ažurirati: ')
#     select_table_query = '''SELECT * FROM Korisnici WHERE id=?'''
#     database_name = 'LoginPodaci.db'

#     try:
#         sc = sqlite3.connect(database_name)
#         cursor = sc.cursor()
#         cursor.execute(select_table_query,(id,))
#         records = cursor.fetchall()
#         for record in records:
#             print(f'Ime: {record[1]} - Prezime: {record[2]}')
#         cursor.close()
#     except sqlite3.Error as e:
#         print('Pogreška kod spajanja na bazu')
#     finally:
#         if sc: 
#             sc.close()
#     ime = input('Unesite ažurirano ime korisnika: ')
#     update_table_query = '''UPDATE Korisnici
#                             SET name=?
#                             WHERE id =?'''
 
#     database_name = 'LoginPodaci.db'
 
#     try:
#         sc=sqlite3.connect(database_name)
#         cursor=sc.cursor()
#         cursor.execute(update_table_query,(f'{ime}',id))
#         sc.commit()
#         cursor.close()
#     except sqlite3.Error as e:
#         print('Pogreska kod spajanja na bazu',e)
#     finally:
#         if sc:
#             sc.close()
#     print('Ime korisnika je ažurirano')
#     go_back = input('Za povratak na Upravljanje računima pritsite tipku Enter ')
#     clear()
#     Acc_Managment()


# def update_surname():
#     id = input('Unesite id korisnika čije prezime želite ažurirati: ')
#     select_table_query = '''SELECT * FROM Korisnici WHERE id=?'''
#     database_name = 'LoginPodaci.db'

#     try:
#         sc = sqlite3.connect(database_name)
#         cursor = sc.cursor()
#         cursor.execute(select_table_query,(id,))
#         records = cursor.fetchall()
#         for record in records:
#             print(f'Ime: {record[1]} - Prezime: {record[2]}')
#         cursor.close()
#     except sqlite3.Error as e:
#         print('Pogreška kod spajanja na bazu')
#     finally:
#         if sc: 
#             sc.close()
#     prezime = input('Unesite ažurirano prezime korisnika: ')
#     update_table_query = '''UPDATE Korisnici
#                             SET surname=?
#                             WHERE id =?'''
 
#     database_name = 'LoginPodaci.db'
 
#     try:
#         sc=sqlite3.connect(database_name)
#         cursor=sc.cursor()
#         cursor.execute(update_table_query,(f'{prezime}',id))
#         sc.commit()
#         cursor.close()
#     except sqlite3.Error as e:
#         print('Pogreska kod spajanja na bazu',e)
#     finally:
#         if sc:
#             sc.close()
#     print('Prezime korisnika je ažurirano')
#     go_back = input('Za povratak na Upravljanje računima pritsite tipku Enter ')
#     clear()
#     Acc_Managment()
    
# def update_passkey():
#     id = input('Unesite id korisnika čiju lozinku želite ažurirati: ')
#     select_table_query = '''SELECT * FROM Korisnici WHERE id=?'''
#     database_name = 'LoginPodaci.db'

#     try:
#         sc = sqlite3.connect(database_name)
#         cursor = sc.cursor()
#         cursor.execute(select_table_query,(id,))
#         records = cursor.fetchall()
#         for record in records:
#             print(f'Ime: {record[1]} - Prezime: {record[2]} - passkey: {record[3]}')
#         cursor.close()
#     except sqlite3.Error as e:
#         print('Pogreška kod spajanja na bazu')
#     finally:
#         if sc: 
#             sc.close()
#     passkey = input('Unesite ažuriranu lozinku korisnika: ')
#     update_table_query = '''UPDATE Korisnici
#                             SET passkey=?
#                             WHERE id =?'''
 
#     database_name = 'LoginPodaci.db'
 
#     try:
#         sc=sqlite3.connect(database_name)
#         cursor=sc.cursor()
#         cursor.execute(update_table_query,(f'{passkey}',id))
#         sc.commit()
#         cursor.close()
#     except sqlite3.Error as e:
#         print('Pogreska kod spajanja na bazu',e)
#     finally:
#         if sc:
#             sc.close()
#     print('Lozinka korisnika je ažurirana')
#     go_back = input('Za povratak na Upravljanje računima pritsite tipku Enter ')
#     clear()
#     Acc_Managment()
            
# def update_email():
#     id = input('Unesite id korisnika čiji email želite ažurirati: ')
#     select_table_query = '''SELECT * FROM Korisnici WHERE id=?'''
#     database_name = 'LoginPodaci.db'

#     try:
#         sc = sqlite3.connect(database_name)
#         cursor = sc.cursor()
#         cursor.execute(select_table_query,(id,))
#         records = cursor.fetchall()
#         for record in records:
#             print(f'Ime: {record[1]} - Prezime: {record[2]} - email: {record[4]}')
#         cursor.close()
#     except sqlite3.Error as e:
#         print('Pogreška kod spajanja na bazu')
#     finally:
#         if sc: 
#             sc.close()
#     email = input('Unesite ažurirani email korisnika: ')
#     update_table_query = '''UPDATE Korisnici
#                             SET email=?
#                             WHERE id =?'''
 
#     database_name = 'LoginPodaci.db'
 
#     try:
#         sc=sqlite3.connect(database_name)
#         cursor=sc.cursor()
#         cursor.execute(update_table_query,(f'{email}',id))
#         sc.commit()
#         cursor.close()
#     except sqlite3.Error as e:
#         print('Pogreska kod spajanja na bazu',e)
#     finally:
#         if sc:
#             sc.close()
#     print('Email korisnika je ažuriran')
#     go_back = input('Za povratak na Upravljanje računima pritsite tipku Enter ')
#     clear()
#     Acc_Managment()

# def update_brtel():
#     id = input('Unesite id korisnika čiji broj telefona želite ažurirati: ')
#     select_table_query = '''SELECT * FROM Korisnici WHERE id=?'''
#     database_name = 'LoginPodaci.db'

#     try:
#         sc = sqlite3.connect(database_name)
#         cursor = sc.cursor()
#         cursor.execute(select_table_query,(id,))
#         records = cursor.fetchall()
#         for record in records:
#             print(f'Ime: {record[1]} - Prezime: {record[2]} - email: {record[4]} - Broj telefona: {record[5]}')
#         cursor.close()
#     except sqlite3.Error as e:
#         print('Pogreška kod spajanja na bazu')
#     finally:
#         if sc: 
#             sc.close()
#     while True:
#         try:
#             br_tel= int(input('Unesite ažurirani broj telefona korisnika: '))
#             break
#         except:
#             print('Neispravan unos!')
#             continue
#     update_table_query = '''UPDATE Korisnici
#                             SET br_tel=?
#                             WHERE id =?'''
 
#     database_name = 'LoginPodaci.db'
 
#     try:
#         sc=sqlite3.connect(database_name)
#         cursor=sc.cursor()
#         cursor.execute(update_table_query,(f'{br_tel}',id))
#         sc.commit()
#         cursor.close()
#     except sqlite3.Error as e:
#         print('Pogreska kod spajanja na bazu',e)
#     finally:
#         if sc:
#             sc.close()     
#     print('Broj telefona korisnika je ažuriran')
#     go_back = input('Za povratak na Upravljanje računima pritsite tipku Enter ')
#     clear()
#     Acc_Managment()


def delete_racun():
    print('1. Izbriši određenog korisnika')
    print('2. Izbriši CIJELU tablicu')
    while True:
        odabir = input('Unesite željenu opciju za brisanje: ')
        if odabir == '1':
            delete_user()
            break
        elif odabir == '2':
            delete_all()
            break
        else:
            print('Neispravan unos!')
            continue

def delete_user():
    while True:
        id = input('Unesite id korisnika kojeg želite ukloniti iz sustava: ')
        security = input(f'Ovaj korak se ne može poništit jeste li sigurni da želite ukloniti korisnika {id}? d/n: ')
        if security.lower() == 'd':
            possibleKey = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            SecurityKey = random.choices(possibleKey, k=5)
            securityQuestion = ''.join(SecurityKey)
            print(securityQuestion)
            SecurityAnswer = input('Unesite sigurnosni kod za brisanje korisnika: ')
            if SecurityAnswer == securityQuestion:
                delete_something_from_table_query  = '''DELETE FROM Korisnici WHERE id=?'''
                database_name = 'LoginPodaci.db'
                try:
                    sc=sqlite3.connect(database_name)
                    cursor=sc.cursor()
                    cursor.execute(delete_something_from_table_query,(id,))
                    sc.commit()
                    cursor.close()
                except sqlite3.Error as e:
                    print('Pogreska kod spajanja na bazu',e)
                finally:
                    if sc:
                        sc.close()
                clear()
                print('Korisnik je uspješno uklonjen iz sustava!')
                Acc_Managment()
                break
            else:
                print('Neispravno ste unijeli sigurnosni kod!')
                continue
        elif security.lower() == 'n':
            print('Odustali ste od uklanjanja korisnika!')
            Acc_Managment()
            break
        else:
            print('Neispravan unos!')
            continue
        
def delete_all():
    while True:
        secQ = input('Jeste li sigurni da želite izbrisati CIJELU tablicu. Ovaj postupak se NE može poništit. d/n: ')
        if secQ.lower() == 'n':
            clear()
            print('Odustali ste od brisanja cijele tablice!')
            Acc_Managment()
            break
        elif secQ.lower() == 'd':
            possibleKey = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            SecurityKey = random.choices(possibleKey, k=10)
            securityQuestion = ''.join(SecurityKey)
            print(securityQuestion)
            secQA = input('Unesite sigurnosni kod za brisanje CIJELE tablice: ')
            if secQA == securityQuestion:
                delete_everything_from_table_query = '''DELETE FROM Korisnici'''
                database_name = 'LoginPodaci.db'
 
                try:
                    sc=sqlite3.connect(database_name)
                    cursor=sc.cursor()
                    cursor.execute(delete_everything_from_table_query)
                    sc.commit()
                    cursor.close()
                except sqlite3.Error as e:
                    print('Pogreska kod spajanja na bazu',e)
                finally:
                    if sc:
                        sc.close()
                clear()
                print('Uspješno ste izbrisali cijelu tablicu!')
                Acc_Managment()
                break
            else:
                clear()
                print('Neispravno ste unijeli sigurnosni kod!')
                Acc_Managment()
                break
              

MainMeni()


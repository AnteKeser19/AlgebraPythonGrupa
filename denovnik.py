class Korisnik:
    def __init__(self, username, password, level, razredi=None):
        self.username = username
        self.password = password
        self.level = level
        self.razredi = razredi if razredi is not None else []

class Predmet:
    def __init__(self, id_predmeta, naziv, nastavnik):
        self.id_predmeta = id_predmeta
        self.naziv = naziv
        self.nastavnik = nastavnik

class Ocjena:
    def __init__(self, id_ucenika, id_predmeta, ocjena, datum):
        self.id_ucenika = id_ucenika
        self.id_predmeta = id_predmeta
        self.ocjena = ocjena
        self.datum = datum

def login():
    username = input("Unesite korisničko ime: ")
    password = input("Unesite lozinku: ")
    # Provjera korisnika i lozinke
    return korisnik

def admin_izbornik():
    print("1. Dodaj korisnika")
    print("2. Ukloni korisnika")
    print("3. Dodaj predmet")
    print("4. Ukloni predmet")
    print("5. Dodaj ocjenu")
    print("6. Ukloni ocjenu")
    print("7. Prikazi sve razrede")
    print("8. Prikazi sve ocjene")
    print("9. Prikazi sve korisnike")
    print("0. Odjava")


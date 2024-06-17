Sve_ocjene = [5,4,2,3,1,1,2,5,4,5,3,2,5,4,5,2,4]

# odlican = 5
# vrlo_dobar = 4
# dobar = 3
# dovoljan = 2
# nedovoljan = 1


odlican = Sve_ocjene.count(5)
vrlo_dobar = Sve_ocjene.count(4)
dobar = Sve_ocjene.count(3)
dovoljan = Sve_ocjene.count(2)
nedovoljan = Sve_ocjene.count(1)


print(f'Odlicnih u razredu je: {odlican},vrlo dobrih: {vrlo_dobar},dobrih: {dobar},dovoljnih: {dovoljan} i nedovoljnih: {nedovoljan}')

#Manje od 50% je 1 , 50-60% je 2, 60-70% je 3, 70-80% je 4, 80-100% je 5

def izracunaj_ocjenu():
    postotak = (bodovi/ 100) * 100
    if postotak <50:
        return 1
    elif 50 <= postotak <60:
        return 2
    elif 60 <= postotak <70:
        return 3
    elif 70 <= postotak <80:
        return 4
    else:
        return 5

ocjene_u_bodovima = [85,72,55,63,25,44,51,77,98,79,92,66,59,81,72,90,52,77,328]

for bodovi in ocjene_u_bodovima:
    ocjena = izracunaj_ocjenu()
    print(f"Za {bodovi} bodova, ocjena je {ocjena}")













racun_broj='R-1-2024-01'
racun_datum_izdavanja='14.05.2024'

racun_stavke={
    'Mlijeko':1.35,
    'Kruh':1.5,
    'Zimska':18.3,
    'Gouda':8.90
}

racun_ukupan_iznos=0

for stavka in racun_stavke.values():
    racun_ukupan_iznos+=stavka

racun_pdv=racun_ukupan_iznos*0.25
print()
print('*'*50)
print(f'\n\tRacun:\t\t{racun_broj}')
print(f'\n\tDatum:\t\t{racun_datum_izdavanja}\n')
print('-'*50)
print('\n\tProizvod\t\tCijena')
for proizvod, cijena in racun_stavke.items():
    print(f'\t{proizvod:<20}\t{cijena:<10}')
print()
print('-'*50)
print(f'\n\tIznos bez PDV:\t\t{racun_ukupan_iznos:.2f}')
print(f'\n\tIznos PDV-a:\t\t{racun_pdv:.2f}')
print(f'\n\tIznos sa PDV:\t\t{racun_ukupan_iznos+racun_pdv:.2f}')
print()
print('*'*50)

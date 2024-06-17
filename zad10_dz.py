# Zadatak:
# Napisi program kojim ćes unijeti datum svog rodjendana i koji će ti ispisati:
# Koliko imas godina
# Koliko je dana ostalo do tvog sljedeceg rodjendana
# Koliko dana imas do mirovine

import datetime as dt
from dateutil.relativedelta import relativedelta

#datum_rodjenja = input('Unesite datum rodjenja u obliku DD.MM.YYYY: ')
datum_rodjenja = '01.05.1988.'
datum_split=datum_rodjenja.split(sep='.')
datum_rodjenja_formatiran=dt.date(int(datum_split[2]),int(datum_split[1]),int(datum_split[0]))

danas=dt.datetime.now()
rdelta = relativedelta(danas, datum_rodjenja_formatiran)
print()
print(f'Imate {rdelta.years} godina, {rdelta.months} mjeseci i {rdelta.days} dana.')


def sljedeci_rodjendan(rodjendan, danas=danas):
    rodj_ova_god = dt.datetime(danas.year, rodjendan.month, rodjendan.day)
    rodj_slj_god = dt.datetime(danas.year+1, rodjendan.month, rodjendan.day)

    return ((rodj_ova_god if rodj_ova_god > danas else rodj_slj_god) - danas).days

slj_rodj=sljedeci_rodjendan(datum_rodjenja_formatiran, danas)

print(f'Sljedeci rodjendan Vam je za {slj_rodj} dana.')

datum_mirovine=dt.datetime(datum_rodjenja_formatiran.year+65, datum_rodjenja_formatiran.month, datum_rodjenja_formatiran.day)
do_mirovine=relativedelta(datum_mirovine, danas)

print(f'Do mirovine imate {do_mirovine.years} godina, {do_mirovine.months} mjeseci i {do_mirovine.days} dana.')
print()
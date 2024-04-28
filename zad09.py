# Potrošnja auta = x na 100km
# Cijena goriva 1.45€ po litri
#koliko košta 1km vožnje?
# Mjesečni trošak (koliko dana osoba radi) i koliko joj je udaljen posao

Potrosnja = float(input('Kolika je potrošnja vašeg automobila?'))
cijena_goriva = 1.45
Broj_radnih_dana = int(input('Koliko dana u mjesecu radite?'))
UdaljenostOdPosla = int(input('Koliko ste udaljeni od vašeg posla?'))

Koliko_kosta_kilometar_voznje = Potrosnja /100 * cijena_goriva
Mjesecna_kilometraza_do_posla = UdaljenostOdPosla * Broj_radnih_dana

Mjesecni_trosak = Mjesecna_kilometraza_do_posla / Koliko_kosta_kilometar_voznje
print(Mjesecni_trosak)
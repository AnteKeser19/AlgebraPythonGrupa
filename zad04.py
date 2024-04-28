#izracun mjesecne potrosne el.energije te cijene el.energije koju
#potrosi mikrovalna snage 1,3kw ako se koristi 2 sata dnevno
#mjesec ima 30 dana, od 24h koristimo 2h
#12c/kwh je cijena energije

potrosnja_u_1h = 1.3
sati_koristeno = 2
broj_dana = 30
cijena_energije_u_eurima = 0.12
dnevna_potrosnja = potrosnja_u_1h*sati_koristeno
mjesecna_potrosnja = dnevna_potrosnja*broj_dana
mjesecni_racun = cijena_energije_u_eurima*mjesecna_potrosnja

print('Mikrovalna u mjesec dana potrosi:',mjesecni_racun,'eura')

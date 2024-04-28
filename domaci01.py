# U trgovini mozete skupljati bodove za popust
# svakih 10 potrosenih eura dobijate 1 bod
# kada skupite 10 bodova, mozete ih zamijenit za 10% popusta pri kupovini do 100€
# ako unesete ostvarene bodove i vaš zadnji račun na kojeg primjenjuete popust, 
# napisite koliko je prodavac od vas za tih 10% popusta dotada dobio novaca, odnosno zaradio u odnosu na koji ste vi "ustedjeli"
# koristenjem tog popusta

vrijednost_1boda_u_eurima = 10 #Koliko vrijedi 1 bod u eurima
vrijednost_popusta = 10 # Iznos popusta 
vrijednost_10_bodova_u_eurima = vrijednost_1boda_u_eurima * vrijednost_popusta 

Moj_racun_pri_kupovini_u_eurima = int(input('Unesite koliko smo novaca potrošili pri kupovini '))
ostvareni_popust = Moj_racun_pri_kupovini_u_eurima / vrijednost_popusta
zarada_prodavača = vrijednost_10_bodova_u_eurima + Moj_racun_pri_kupovini_u_eurima - ostvareni_popust
ustedjeni_novac = Moj_racun_pri_kupovini_u_eurima / vrijednost_popusta

print(f'Prodavač je zaradio {zarada_prodavača} €,a mi smo uštedjeli {ustedjeni_novac} €')


# {}:.0f .2f zakrouzivanje decimala prilikom ispisa

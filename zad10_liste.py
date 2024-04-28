lista=[156, 'rijec', 'ovo je recenica', True, 3.14, 65]
 
#print(lista[2])
 
#print(lista)
 
#print(lista[1][3])
 
for mate in lista:
    print(mate)
 
print()
for test in lista:
    test=str(test)+str(2)
    print(test)
 
 
# tekst='mate'
# tekst2=2
# tekstskupa=tekst+tekst2
# print(tekstskupa)
 
lista2=[156,False, 3.14, 65] # 'rijec', 'ovo je recenica',
 
print()
for test in lista2:
    test=test+2
    print(test)
print()
 
niz=[]
print(niz)
 
niz.append(5)
print(niz)
niz.append('tekst')
print(niz)
#niz.clear()
br_elemenata_tekst=niz.count('tekst')
print(br_elemenata_tekst)
print(niz)
duzina_niza=len(niz)
print(duzina_niza)
duzina_liste=len(lista)
print(duzina_liste)
 
l_a=[1, 2, 3]
a=5
b=a
print(a,b)
 
c='mate'
d=c
print(c, d)
 
l_b=l_a
print(l_a, l_b)
l_b[1]=5
print(l_b)
print(l_a)
 
l_c=[1,2,3]
l_d=l_c.copy()
l_d[1]=5
print(l_d)
print(l_c)
 
print(lista)
print(l_c)
lista.extend(l_c)
print(lista)
 
pozicija314=lista.index(3.14)
print(pozicija314)
 
lista.insert(2,'veznik')
print(lista)
 
lista.pop(4) #ukloni element na indeksu 4
print(lista)
 
lista.remove(2) #ukloni broj 2
print(lista)
 
lista.reverse()
print(lista)
 
lista2.sort(reverse=True)
print(lista2)
 
print(range(5))
 
for indeks in range(5):
    print(indeks)
 
for indeks in range(len(lista2)):
    print(indeks, lista2[indeks])
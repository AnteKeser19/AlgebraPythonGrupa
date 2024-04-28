# broj_bodova=[53,42,73,94]
# for i in range (len(broj_bodova)):
#     ocjena = int(((broj_bodova[i] -50) // 12.5) +2)
#     print(ocjena)

max_bodova = 100

broj_bodova=[53,42,73,94]
for i in range (len(broj_bodova)):
    ocjena = int(((broj_bodova[i] - (max_bodova/2)) // (max_bodova/8)) +2)
    print(ocjena)

# v1
# try:
#     with open('adresar.txt','r') as fr:
#         fd=fr.read()
#         print(fd)
# except Exception as e:
#     print(f'Dogodila se greska {e}')
 
 
try:
    with open('adresar.txt','r') as fr:
        for red in fr:
            #print(red,end='')
            dijelovi_reda=red.split(';')
            #print(dijelovi_reda)
            print(f'ID: {dijelovi_reda[0]}\tIme: {dijelovi_reda[1]}\tPrezime: {dijelovi_reda[2]}\tMob: {dijelovi_reda[3][:-1]}')
except Exception as e:
    print(f'Dogodila se greska {e}')
 
 
 
#v1
# counter=1
# while True:
#     ime=input('Unesite ime kontakta: ')
#     prezime=input('Unesite prezime kontakta: ')
#     mob=input('Unesite broj mobitela: ')
 
#     fw=open('adresar.txt','w')
#     fw.write(f'{counter};{ime};{prezime};{mob}')
#     counter+=1
#     fw.close()
 
#     if input('x za izlaz').lower() == 'x':
#         break
 
 
# v2
# counter=1
# fw=open('adresar.txt','w')
# while True:
#     ime=input('Unesite ime kontakta: ')
#     prezime=input('Unesite prezime kontakta: ')
#     mob=input('Unesite broj mobitela: ')
 
 
#     fw.write(f'{counter};{ime};{prezime};{mob}')
#     counter+=1
 
 
#     if input('x za izlaz').lower() == 'x':
#         break
 
# fw.close()
 
 
 
 
#v3
# counter=1
# while True:
#     ime=input('Unesite ime kontakta: ')
#     prezime=input('Unesite prezime kontakta: ')
#     mob=input('Unesite broj mobitela: ')
 
#     fw=open('adresar.txt','a')
#     fw.write(f'{counter};{ime};{prezime};{mob}\n')
#     counter+=1
#     fw.close()
 
#     if input('x za izlaz').lower() == 'x':
#         break
 
 
 
#v4
# counter=1
# while True:
#     ime=input('Unesite ime kontakta: ')
#     prezime=input('Unesite prezime kontakta: ')
#     mob=input('Unesite broj mobitela: ')
 
#     try:
#         fw=open('adresar.txt','a')
#         fw.write(f'{counter};{ime};{prezime};{mob}\n')
#         counter+=1
#     except Exception as e:
#         print(f'Dogodila se greska {e}')
#     finally:
#         fw.close()
 
#     if input('x za izlaz').lower() == 'x':
#         break
 
 
#v5
counter=1
while True:
    ime=input('Unesite ime kontakta: ')
    prezime=input('Unesite prezime kontakta: ')
    mob=input('Unesite broj mobitela: ')
 
    try:
        with open('adresar.txt','a') as fw:
            fw.write(f'{counter};{ime};{prezime};{mob}\n')
            counter+=1
    except Exception as e:
        print(f'Dogodila se greska {e}')
 
 
    if input('x za izlaz').lower() == 'x':
        break
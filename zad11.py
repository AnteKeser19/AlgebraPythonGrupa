file_writer = open('ime.txt','w')
ime=input('Unesite vase ime: ')
file_writer.write(ime)
file_writer.close()
 
file_reader=open('ime.txt','r')
file_data=file_reader.read()
file_reader.close()
 
print(f'Sadrzaj datoteke je\n{file_data}')
 
mate_cita=open('ime.txt','r')
matini_podaci=mate_cita.read()
mate_cita.close()
 
print(f'Sadrzaj datoteke je\n{matini_podaci}')
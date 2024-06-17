import sqlite3

insert_into_table_query='''INSERT INTO Employees (name, email)
                            VALUES (?,?)'''

database_name='TvrtkaDb.db'

lista_radnika=[
    ('Mate Matic','mmatic@mail.com'),
    ('Ana Anic','aanic@hotmail.com'),
    ('Jure Juric','jjuric@brzi.hr')
]

try:
    sc=sqlite3.connect(database_name)
    cursor=sc.cursor()
    for radnik in lista_radnika:
        cursor.execute(insert_into_table_query,radnik)

    sc.commit()
    cursor.close()
except sqlite3.Error as e:
    print('Pogreska kod spajanja na bazu',e)
finally:
    if sc:
        sc.close()
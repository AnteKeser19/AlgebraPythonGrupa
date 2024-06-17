import sqlite3

delete_something_from_table_query='''DELETE FROM Employees WHERE id=?'''
delete_everything_from_table_query='''DELETE FROM Employees'''

database_name='TvrtkaDb.db'

try:
    sc=sqlite3.connect(database_name)
    cursor=sc.cursor()
    #cursor.execute(delete_something_from_table_query,(3,))
    cursor.execute(delete_everything_from_table_query)
    sc.commit()
    cursor.close()
except sqlite3.Error as e:
    print('Pogreska kod spajanja na bazu',e)
finally:
    if sc:
        sc.close()


# osmisliti jedan program u pythonu koji ce koristeci funkcije i sustav menija
# odraditi sve ove korake koje smo sada "rucno" radili kroz razlicite datoteke

#kreirati meni - upisi korisnika, iscitaj podatke u bazi, pronadji sve mate u bazi podataka

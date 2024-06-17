import sqlite3

select_table_query='''SELECT * FROM Employees WHERE id=?'''

database_name='TvrtkaDb.db'

try:
    sc=sqlite3.connect(database_name)
    cursor=sc.cursor()
    cursor.execute(select_table_query,(2,)) #tuple od jednog clana mora imati zarez "(1,)"
    records=cursor.fetchall()
    #print(records)
    for record in records:
        print(record)
        #print(f'Ime: {record[1]} - Email: {record[2]}')
    cursor.close()
except sqlite3.Error as e:
    print('Pogreska kod spajanja na bazu')
finally:
    if sc:
        sc.close()
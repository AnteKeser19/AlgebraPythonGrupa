import sqlite3

create_table_query='''CREATE TABLE IF NOT EXISTS Employees (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE);'''

database_name='TvrtkaDb.db'

try:
    sc=sqlite3.connect(database_name) #sc je sqlite connection
    cursor=sc.cursor()
    cursor.execute(create_table_query)
    sc.commit()
    cursor.close()
except sqlite3.Error as e:
    print('Pogreska kod spajanja na bazu')
finally:
    if sc:
        sc.close()
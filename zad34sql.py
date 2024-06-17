import sqlite3

select_query="SELECT sqlite_version();"

try:
    sqliteConnection=sqlite3.connect('SQLite_Python.db')
    cursor=sqliteConnection.cursor()
    cursor.execute(select_query)
    records=cursor.fetchall()
    print('SQL verzija',records)
    cursor.close()
except sqlite3.Error as e:
    print('Pogreska kod spajanja na bazu')
finally:
    if sqliteConnection:
        sqliteConnection.close()
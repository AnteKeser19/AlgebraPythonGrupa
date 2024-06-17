import sqlite3

update_table_query='''UPDATE Employees
                            SET name=?, email=?
                            WHERE id=?'''

database_name='TvrtkaDb.db'

try:
    sc=sqlite3.connect(database_name)
    cursor=sc.cursor()
    cursor.execute(update_table_query,('Ana Anic Matic','aanic@hotmailcom',2))
    sc.commit()
    cursor.close()
except sqlite3.Error as e:
    print('Pogreska kod spajanja na bazu',e)
finally:
    if sc:
        sc.close()
import sqlite3
conn=sqlite3.connect('testing.db')

cursor=conn.execute('select * from works')
people=list(cursor)

for i in cursor:
    print(i)
    
    
conn.close()
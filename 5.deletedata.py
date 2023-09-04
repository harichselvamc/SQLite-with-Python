import sqlite3
conn=sqlite3.connect('sample.db')

cursor=conn.execute('select * from user')
conn.execute("DELETE FROM USER WHERE id=4")

for i in cursor:
    print(i)
    
    
conn.close()
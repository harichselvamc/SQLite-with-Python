import sqlite3
conn=sqlite3.connect('sample.db')
conn.execute('update user set name="harich"where id=2')
cursor=conn.execute('select * from user')


for i in cursor:
    print(i)
    
    
conn.close()
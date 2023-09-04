import sqlite3
conn=sqlite3.connect('sample.db')
cursor=conn.execute('select * from user')
data=list(cursor)
print(cursor)
for i in cursor:
    print(i)
    
    
conn.close()
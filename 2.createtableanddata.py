import sqlite3
conn=sqlite3.connect("sample.db")
print("created ")
conn.execute('''create table userss (id int primary key  not null,name text not null )''')

print("Table created successfully")

conn.execute("insert into userss (id,name)values(1,'hari')");
conn.execute("insert into userss (id,name)values(2,'riya')");
conn.execute("insert into userss (id,name)values(3,'max')");

conn.commit()
conn.close()
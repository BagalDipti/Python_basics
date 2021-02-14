
#-------------Python sqlite3 Connectivity----------------------------------------------
import sqlite3 as sq

con=sq.connect("database1.db")
cur=con.cursor()
cur.execute("create table student(name text)")
cur.execute("create table employee(id int, name text)")
l=[(105,'pqr'),(103,'lmn'),(106,'hel')]
cur.executemany("insert into employee values(?,?)",l)
data=cur.execute("select * from employee")
for i in data:
    print(i[0],i[1])


cur.execute("select * from employee")
data=cur.fetchall()
for i in data:
    print(i[0],i[1])


cur.execute("select * from employee where id=?",[102])
data=cur.fetchone()
print(data)

'''

cur.execute("delete from employee where id=105")
data=cur.fetchone()
print(data)


'''

con.commit()
con.close()

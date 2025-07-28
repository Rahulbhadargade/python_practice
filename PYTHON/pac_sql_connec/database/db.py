import sqlite3 as sql

connect = sql.connect('Store.db')
cursor = connect.cursor()

cursor.execute(
    "create table if not exists Emp(name varchar, age number, sal number)")
cursor.execute("insert into Emp values('Rahul', 22, 500000)")
cursor.execute("insert into Emp values('Divya', 22, 10000000)")
cursor.execute("insert into Emp values('Raj', 20, 700000)")

connect.commit()

data = cursor.execute("select *  from Emp")
print(list(data))

connect.close()


import sqlite3 as sql

connect = sql.connect('Values.db')
cursor = connect.cursor()

def create_table():
    cursor.execute(
        "create table if not exists Details(addition number, " \
        "subtraction number)")

def insert(a, b):
    cursor.execute(f"insert into Details values({a}, {b})")
    connect.commit()

def display():
    print(list(cursor.execute("select * from Details")))

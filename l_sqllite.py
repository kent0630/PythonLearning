#!/usr/bin/python
# encoding=utf-8

import sqlite3 #导入模块

cx = sqlite3.connect("test.db")

cu=cx.cursor()
# cu.execute("""create table catalog ( id integer primary key, pid integer, name varchar(10) UNIQUE )""")
# cu.execute("insert into catalog values(2, 0, 'name2')")
# cu.execute("insert into catalog values(3, 0, 'helloworld')")
for t in[(4, 0,'Yu'),(5, 0, 'Xu')]:
    cx.execute("insert into catalog values (?,?,?)", t)
cx.commit()
# select
cu.execute("select * from catalog")
print cu.fetchall()
cu.close()
cx.close()

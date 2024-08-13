import pymysql
connection=pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='db1'
)
cursor=connection.cursor()
cursor.execute("drop table if  exists   employee2")
sql=""" create table employee2 (
    empno int(11),
    name varchar(100),
    salary int(11))"""
cursor.execute(sql)
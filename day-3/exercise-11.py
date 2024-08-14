import pymysql;
connection = pymysql.connect(
  host='localhost',
  user='root',
  password='',
  database='db1'
);
cursor = connection.cursor();
cursor.execute("select * from employee");
data = cursor.fetchone();
print (data);
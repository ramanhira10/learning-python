import pymysql;
connection = pymysql.connect(
  host='localhost',
  user='root',
  password='',
  database='db1'
);
cursor = connection.cursor();
cursor.execute("select * from employee");
data = cursor.fetchall();
print (data);
for row in data:
  emp_id = row[0];
  name = row[1];
  salary = row[2];
  print (emp_id, name, salary);
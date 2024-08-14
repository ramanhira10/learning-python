import pymysql
connection = pymysql.connect(
  host='localhost',
  user='root',
  password='',
  db='db1'
);
try:
  with connection.cursor() as cursor:
    sql = "insert into employee (emp_id, name, salary) values (222, 'Ram', 5000)";
    try:
      cursor.execute(sql);
      print ("data inserted");
    except:
      print ("data not inserted");
  connection.commit();
finally:
  connection.close();
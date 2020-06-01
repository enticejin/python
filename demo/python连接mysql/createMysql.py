import mysql.connector

'''
connect = mysql.connector.connect(
    host="127.0.0.1",
    user='root',
    password='123456',
)

cursor = connect.cursor()
#创建数据库名称
cursor.execute("CREATE DATABASE pythonMysql")
'''
'''
#连接数据库
connect = mysql.connector.connect(host="127.0.0.1", user="root", password="123456", )
#初始化
mycursor  = connect.cursor()
#执行sql语句
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
'''
'''
my_db = mysql.connector.connect(host="127.0.0.1", user="root", password="123456", database="pythonMysql")
cursor = my_db.cursor()
cursor.execute("CREATE TABLE sites (name varchar(255), url varchar(255))")
'''
'''
connect = mysql.connector.connect(host="127.0.0.1", user="root", password="123456", database="pythonMysql", )
cursor = connect.cursor()
cursor.execute("show tables")
for x in cursor:
    print(x)
'''
'''
connect = mysql.connector.connect(host="127.0.0.1", user="root", password="123456", database="pythonMysql", )
cursor = connect.cursor()
cursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")
'''
'''
connect = mysql.connector.connect(host="127.0.0.1", user="root", password="123456", database="pythonMysql", )
sql = "insert into sites (name, url) values(%s, %s)"
val = ('RUNOOB',"https://www.runoob.com")
cursor = connect.cursor()
cursor.execute(sql, val)
connect.commit()
print(cursor.rowcount,"记录插入成功！")
'''
'''
connect = mysql.connector.connect(host="127.0.0.1", user="root", password="123456", database="pythonMysql", )
sql="insert into sites (name, url) values (%s, %s)"
val=[
    ('Google', 'https://www.google.com'),
  ('Github', 'https://www.github.com'),
  ('Taobao', 'https://www.taobao.com'),
  ('stackoverflow', 'https://www.stackoverflow.com/')
]
cursor = connect.cursor()
cursor.executemany(sql, val)
connect.commit()
print(cursor.rowcount, "记录插入成功！")
'''
'''
connect = mysql.connector.connect(host="127.0.0.1", user="root", password="123456", database="pythonMysql", )
sql="insert into sites (name, url) values (%s, %s)"
val = ("Zhihu", "https://www.zhihu.com")
cursor = connect.cursor()
cursor.execute(sql, val)
connect.commit()
print("记录插入成功！", cursor.lastrowid)
'''
'''
#查询数据库
connect = mysql.connector.connect(host="127.0.0.1", user="root", password="123456", database="pythonMysql", )
cursor = connect.cursor()
#cursor.execute("select * from sites")
cursor.execute("select name, url from sites")
fetchall = cursor.fetchall()
for x in fetchall:
    print(x)
# print("**************")
# fetchone = cursor.fetchone()
# print(fetchone)
'''


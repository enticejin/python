import mysql.connector
#打开数据库
db = mysql.connector.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='sys', )
#使用cursor创建一个游标对象
cursor = db.cursor()

#使用excute执行sql查询

ex= cursor.execute('SELECT * FROM SYS_CONFIG')
data = cursor.fetchall()

print(data)
cursor.close()
db.close

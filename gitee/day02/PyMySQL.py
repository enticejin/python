import pymysql

db = pymysql.connect('localhost', user='root', password='123456', database='sys')

cursor = db.cursor()

execute = cursor.execute('select * from sys_config where value like "%OFF%"')

fetchall = cursor.fetchall()
print(fetchall)
cursor.close()
db.close()


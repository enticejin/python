import MySQLdb
db = MySQLdb.connect(host='127.0.0.1', port=3306, user = 'root', password = '123456', db = 'sys', charset = 'utf8')
cursor = db.cursor()
# 使用execute执行sql查询
cursor.execute('SELECT * FROM sys_config')
# 使用 fetchall() 方法获取s所有数据.
data = cursor.fetchall()
print(data)
cursor.close()
db.close()

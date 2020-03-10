import pymysql

#打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "123456", "test")

#使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据
fetchone = cursor.fetchone()
print("Database version : %s " % fetchone)

# 关闭数据库连接
db.close()

from bottle import route, run


'''
@route('/hello')  # 定义路由，即浏览器访问的地址
def hello():  # 函数名根据功能随意定义吧，只要不使用系统关键字便可，一般推荐按功能命名吧
    return "Hello www.gejin.com"  # 浏览器返回的内容

run(host='127.0.0.1', port=8080)  # 开启服务，端口是8080，授受任何IP地址访问
'''

@route('/test')
def test():
    return "this is a test"

run(host="127.0.0.1", port=8003)

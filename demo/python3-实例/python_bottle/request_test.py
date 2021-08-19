
#从bottle中引入run， request， route
from bottle import run, request, route
#响应get请求的login

@route('/login')
def login():
        '''
        这里不指定方法时，默认就是GET方法
        登陆页面，html代码都是直接从这里返回到网页中去的，如果不带任何方法，此函数将响应
        关于模板的使用，后面课程会讲到
        '''
        return '''
        <html>
        <head>
        </head>
        <body>
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
        </body>
        </html>
    '''
@route('/login', method='POST')
def do_login():
        '''
        函数名字随意定，这里是进行POST动作的，所以用了do_login，函数名不能与前后函数有同名
        登陆动作，这里用了post，也就是当访问login页面，同时带了POST请求时，这个函数将响应
        '''
        username = request.forms.get('username')
        password = request.forms.get('password')
        return '<p>帐号:%s</p><p>密码:%s</p>' %(username,password)
run(host='127.0.0.1', port=8080, debug=True)   #开启服务
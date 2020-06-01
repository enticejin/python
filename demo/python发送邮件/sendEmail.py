
import smtplib,random
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = 'www.403367632@qq.com'  # 发件人邮箱账号
my_pass = '1994owzosdknhrqmbehg0525'  # 发件人邮箱密码
my_user = 'gejinjin0404@foxmail.com'  # 收件人邮箱账号，我这边发送给自己


def generate_verification_code():

    ''' 随机生成6位的验证码 '''

    code_list = []

    for i in range(10): # 0-9数字

        code_list.append(str(i))

    for i in range(65, 91): # A-Z

        code_list.append(chr(i))

    for i in range(97, 123): # a-z

        code_list.append(chr(i))
    myslice = random.sample(code_list, 6)  # 从list中随机获取6个元素，作为一个片断返回

    verification_code = ''.join(myslice) # list to string

    # print code_list

    # print type(myslice)

    return verification_code

def mail():
    ret = True
    try:
        code = generate_verification_code()
        msg = MIMEText('验证码是： '+code, 'plain', 'utf-8')
        msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")


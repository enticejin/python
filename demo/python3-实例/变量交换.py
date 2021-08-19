#输入
x = float(input('输入x值：'))
y = float(input('输入y值：'))

#定义一个中间变量来记录下x值
temp = x
#把y的值赋值给x
x = y
#再把记录下的x值赋值给y
y = temp

print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))

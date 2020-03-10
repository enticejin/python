#输入数字
num1 = input('输入第一个数字')
num2 = input('输入第二个数字')
#将输入的数字转换
num1 = float(num1)
num2 = float(num2)
#将转换后的数字相加
sum = num2 + num1

#显示结果
print("数字{0}与数字{1}相加的结果为：{2}".format(num1, num2, sum))

#上述表达式可以简化成：
print('两数之和为 %.1f' %(float(input('输入第一个数字：'))+float(input('输入第二个数字：'))))
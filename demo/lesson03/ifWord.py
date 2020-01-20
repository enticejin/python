'''
4.1. if 语句
可以有零个或多个 elif 部分，以及一个可选的 else 部分。 关键字 'elif' 是 'else if' 的缩写，
适合用于避免过多的缩进。 一个 if ... elif ... elif ... 序列可以看作是其他语言中的 switch 或 case 语句的替代。

x = int(input("请输入一个整数"))
if x < 0 :
    x = 0
    print('比0小')
elif x ==0:
    print('刚刚好等于0')
elif x == 1:
    print('单数')
else:
    print('大了')
'''
'''
4.2. for 语句
words = ['cat','window','defensetrate']
for word in words:
    print(word, len(word))

'''
'''
4.3. range() 函数  
for i in range(5):
    print(i,end=',')#0,1,2,3,4,  

#默认步长为1
for num in range(5,10):
    print(num, end=',')
#步长设置成2
for i in range(5 , 10 , 2):
    print(i,end=' ')
#步长设置成负数
for i in range(10 , 5 , -1):
    print(i,end=' ')
'''
print(list(range(4))) #[0, 1, 2, 3]
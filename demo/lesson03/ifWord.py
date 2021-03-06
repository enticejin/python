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

print(list(range(4))) #[0, 1, 2, 3]
'''

'''
4.4. break 和 continue 语句，以及循环中的 else 子句
'''
#在范围2到10判断是否是整数,else在循环中，不属于if
'''
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n,'=', x ,'*',n // x)
            break
    else:
        print(n,'是质数')
'''
'''
for num in range(2 , 10):
    if num % 2 == 0:
        print('找到一个偶数是：',num)
        continue
    print(num,'不是偶数')
'''

'''
4.5. pass 语句
pass 语句什么也不做。当语法上需要一个语句，但程序需要什么动作也不做时，可以使用它
while True:
    pass
    
这通常用于创建最小的类:
class MyEmptyClass:
    pass
    
pass 的另一个可以使用的场合是在你编写新的代码时作为一个函数或条件子句体的占位符，
允许你保持在更抽象的层次上进行思考。 pass 会被静默地忽略:
def initlog(*args):
    pass
'''

'''
4.6. 定义函数
我们可以创建一个输出任意范围内 Fibonacci 数列的函数:
def fib(n):
    a,b = 0 , 1
    while a < n:
        print(a , end=' ')
        a, b = b, a + b
    print()
fib(2000)

写一个返回斐波那契数列的列表（而不是把它打印出来）
def fib2(num):
    result = []
    a, b = 0, 1
    while a < num:
        result.append(a)
        a, b = b, a + b
    return result
fib2(100)
'''
'''
4.7. 函数定义的更多形式
4.7.1. 参数默认值
最有用的形式是对一个或多个参数指定一个默认值。这样创建的函数，
可以用比定义时允许的更少的参数调用，比如:
def ask_ok(prompt, retries = 4, reminder= 'Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        if retries < 0:
            raise ValueError('invalid user respose')
        print(reminder)

ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

i =5
def f(arg = i):
    print(arg)

f() #5
i = 6
f() #5 

重要警告： 默认值只会执行一次。这条规则在默认值为可变对象（列表、字典以及大多数类实例）时很重要。
比如，下面的函数会存储在后续调用中传递给它的参数:
def function(a, L = []):
    L.append(a)
    return L
print(function(1))
print(function(2))
print(function(3))
#运行结果：
[1]
[1, 2]
[1, 2, 3]

如果你不想要在后续调用之间共享默认值，你可以这样写这个函数:
def function(a, L = None):
    if L is None:
        L = []
    L.append(a)
    return L

print(function(1))
print(function(2))
print(function(3))
#运行结果
[1]
[2]
[3]
'''

'''
4.7.2. 关键字参数

'''








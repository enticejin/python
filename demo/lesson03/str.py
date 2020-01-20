'''
3.1.2. 字符串

string = '123456'
print(string)
#判断是否全是数字和字符串
string = string+'abc'
print(string.isalnum())
#乘以n表示打印几次
print(string * 3)
#判断索引位置,从0开始
s = string[0]
print(s)
#截取指定片段(含头不含尾)切片的开始总是被包括在结果中，而结束不被包括。这使得 s[:i] + s[i:] 总是等于 s
print(string[2:6])
#len()方法获取字符串长度
print(len(string))
#从头到尾截取字符串
print(string[0:])#方法一
print(string[:])#方法二
'''
'''
3.1.3. 列表
squares = [1,2,3,4,5,6]
print(squares)
#索引和切片
print(squares[0])
print(squares[0:3])
#列表添加元素
squares.append('3')#默认尾部追加
print(squares)
#列表相加
squares = squares + ['a','b','c']
print(squares)
#获取列表长度
print(len(squares))
'''
'''
3.2.走向编程的第一步
当然，我们可以将 Python 用于更复杂的任务，而不是仅仅两个和两个一起添加。 
例如，我们可以编写 斐波那契数列 的初始子序列

a , b = 0 , 1
while a < 1000:
    print(a,end=",")
    a , b = b , a + b
脚注
1
    因为 ** 比 - 有更高的优先级, 所以 -3**2 会被解释成 -(3**2) ，因此结果是 -9. 为了避免这个并且得到结果 9, 你可以用这个式子 (-3)**2.
2
    和其他语言不一样的是, 特殊字符比如说 \n 在单引号 ('...') 和双引号 ("...") 里有一样的意义. 
    这两种引号唯一的区别是，你不需要在单引号里转义双引号 " (但是你必须把单引号转义成 \') ， 反之亦然.
'''



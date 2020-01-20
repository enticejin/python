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
'''
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

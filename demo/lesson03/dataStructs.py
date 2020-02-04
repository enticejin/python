'''
5. 数据结构
5.1. 列表的更多特性¶

列表数据类型还有很多的方法。这里是列表对象方法的清单：

list.append(x)

    在列表的末尾添加一个元素。相当于 a[len(a):] = [x] 。

list.extend(iterable)

    使用可迭代对象中的所有元素来扩展列表。相当于 a[len(a):] = iterable 。

list.insert(i, x)

    在给定的位置插入一个元素。第一个参数是要插入的元素的索引，所以 a.insert(0, x) 插入列表头部， a.insert(len(a), x) 等同于 a.append(x) 。

list.remove(x)

    移除列表中第一个值为 x 的元素。如果没有这样的元素，则抛出 ValueError 异常。

list.pop([i])

    删除列表中给定位置的元素并返回它。如果没有给定位置，a.pop() 将会删除并返回列表中的最后一个元素。
    （ 方法签名中 i 两边的方括号表示这个参数是可选的，而不是要你输入方括号。你会在 Python 参考库中经常看到这种表示方法)。

list.clear()

    删除列表中所有的元素。相当于 del a[:] 。

list.index(x[, start[, end]])

    返回列表中第一个值为 x 的元素的从零开始的索引。如果没有这样的元素将会抛出 ValueError 异常。

    可选参数 start 和 end 是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是 start 参数。

list.count(x)

    返回元素 x 在列表中出现的次数。

list.sort(key=None, reverse=False)

    对列表中的元素进行排序（参数可用于自定义排序，解释请参见 sorted()）。

list.reverse()

    反转列表中的元素。

list.copy()

    返回列表的一个浅拷贝。相当于 a[:] 。
#列方法示例：
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple')) #2
print(fruits.count('app')) #0
print(fruits.index('pear')) #2
print(fruits.index('banana')) #3
print(fruits.index('banana', 4)) #从索引为4开始找元素所在位置
fruits.reverse() #元素反转
print(fruits)
fruits.append('123') #在列表末尾追加元素
print(fruits)
fruits.sort()
print(fruits) #排序
print(fruits.pop())
'''
'''
5.1.1. 列表作为栈使用
列表方法使得列表作为堆栈非常容易，最后一个插入，最先取出（“后进先出”）。
要添加一个元素到堆栈的顶端，使用 append() 。要从堆栈顶部取出一个元素，使用 pop() ，不用指定索引。例如
stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack) #[3, 4, 5, 6, 7]

print(stack.pop()) #7
print(stack.pop()) #6
print(stack.pop()) #5
print(stack) #[3, 4]
'''
'''
5.1.2. 列表作为队列使用
列表也可以用作队列，其中先添加的元素被最先取出 (“先进先出”)；然而列表用作这个目的相当低效。
因为在列表的末尾添加和弹出元素非常快，但是在列表的开头插入或弹出元素却很慢 (因为所有的其他元素都必须移动一位)。
若要实现一个队列， collections.deque 被设计用于快速地从两端操作。例如
from collections import  deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
print(queue)
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue.popleft())

#运行结果
deque(['Eric', 'John', 'Michael', 'Terry'])
deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])
Eric
John
'''

'''
5.1.3. 列表推导式
列表推导式提供了一个更简单的创建列表的方法。常见的用法是把某种操作应用于序列或可迭代对象的每个元素上，
然后使用其结果来创建列表，或者通过满足某些特定条件元素来创建子序列。
squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = list(map(lambda x: x ** 2,range(10)))
print(squares) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = [x ** 2 for x in range(10)] #这种写法更加简洁易读
print(squares) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])) #[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
#上面的例子等价于
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x , y))
print(combs)
vec = [-4, -2, 0, 2, 4]
print([x**2 for x in vec]) #[16, 4, 0, 4, 16]
print([abs(x) for x in vec]) #[4, 2, 0, 2, 4]
print([x for x in vec if x >= 0]) #[0, 2, 4]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit]) #['banana', 'loganberry', 'passion fruit']
print([(x, x **2) for x in range(6)]) #[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem]) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
#列表推导式可以使用复杂的表达式和嵌套函数
from math import pi
print([str(round(pi, i)) for i in range(1,6)]) #['3.1', '3.14', '3.142', '3.1416', '3.14159']
'''
'''
5.1.4嵌套的列表推导式
列表推导式中的初始表达式可以是任何表达式，包括另一个列表推导式
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)
#矩阵的行换成列1：
print([[row[i] for row in matrix] for i in range(4)])
#矩阵的行换成列2：
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
#矩阵的行换成列3：
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
'''

'''
5.2. del 语句
有一种方式可以从列表按照给定的索引而不是值来移除一个元素: 那就是 del 语句。 
它不同于会返回一个值的 pop() 方法。 
del 语句也可以用来从列表中移除切片或者清空整个列表（我们之前用过的方式是将一个空列表赋值给指定的切片）
a = [1,2,3,4,5,6]
#del a[0]
print(a) #[2, 3, 4, 5, 6]
#del a[1:3]
print(a)
del a[:]
print(a)

'''
'''
5.3. 元组和序列
t = 123,456,'hello'
print(t[0])
print(t)
u = t, ('abc','def','ghi')
print(u)
#运行结果
123
(123, 456, 'hello')
((123, 456, 'hello'), ('abc', 'def', 'ghi'))

v = ([1,2,3],['a','b','c'])
print(v) #([1, 2, 3], ['a', 'b', 'c'])

empty = ()
singleTon = 'hello',
print(len(empty))
print(len(singleTon))
print(singleTon)
#运行结果
0
1
('hello',)

'''
'''
5.4. 集合
花括号或 set() 函数可以用来创建集合。注意：要创建一个空集合你只能用 set() 而不能用 {}，
因为后者是创建一个空字典
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) #{'apple', 'pear', 'orange', 'banana'}
print("orange" in basket) #True
print('123' in basket) #False

a = set('123123123654')
b = set('chinese')
print(a)
print(b)
print("**********")
print(a - b) # letters in a but not in b
print(a | b)
print(a & b)
print(a ^ b)  # letters in a or b but not both



a = {x for x in 'abracadabra' if x not in 'abc'}
print(a) #{'r', 'd'}
'''
'''
5.5. 字典
理解字典的最好方式，就是将它看做是一个 键: 值 对的集合，键必须是唯一的（在一个字典中）。
一对花括号可以创建一个空字典：{} 。另一种初始化字典的方式是在一对花括号里放置一些以逗号分隔的键值对，
而这也是字典输出的方式。
tel = {'jack': 4098, 'space' : 4139}
tel['guido'] = 4127
print(tel) #{'jack': 4098, 'space': 4139, 'guido': 4127}
print(tel['jack']) #4098
print(sorted(tel)) #['guido', 'jack', 'space']
print(list(tel)) #['jack', 'space', 'guido']
print('guido' in tel) #True
print('guido' not in tel) #False

#dict() 构造函数可以直接从键值对序列里创建字典
print(dict([('1','name'),('2','body'),('3','head')]))

#字典推导式可以从任意的键值表达式中创建字典
print({x : x ** 2 for x in (2, 4, 6)}) #{2: 4, 4: 16, 6: 36}
#当关键字是简单字符串时，有时直接通过关键字参数来指定键值对更方便
print(dict(sape=4139, guido=4127, jack=4098)) #{'sape': 4139, 'guido': 4127, 'jack': 4098}
'''
'''
5.6. 循环的技巧
当在字典中循环时，用 items() 方法可将关键字和对应的值同时取出
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for key ,value in knights.items():
    print(key, value)
'''
'''
5.7. 深入条件控制
while 和 if 条件句中可以使用任意操作，而不仅仅是比较操作。

比较操作符 in 和 not in 校验一个值是否在（或不在）一个序列里。操作符 is 和 is not 比较两个对象是不是同一个对象，这
只对像列表这样的可变对象比较重要。所有的比较操作符都有相同的优先级，且这个优先级比数值运算符低。
string1,string2,string3 = "" , "TheuesDay" , "1234556"
non_null  = string1 or string2 or string3
print(non_null) #TheuesDay
'''




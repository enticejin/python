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
'''


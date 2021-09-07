#Python3.8·官方文档笔记

##1.1简介
##python的相较于其他语言短很多
        原因：
        1.没有成对的花括号，采用缩进的方式
        2.在一个表达式中可以做很多复杂的操作
        3.不需要预先定义变量和参数

#3. Python 的非正式介绍

    // #表示地板除法
    例如：
    17 // 3 = 5
    解释： 
    表示除法运算执行后只取整数部分，忽略小数部分

    ** #表示乘方
    例如： 
    2 ** 3 = 8 
    解释：
    表示2的3次方运算后等于8
    
    python支持整数和浮点数一起运算
    例如：4.1 * 3 + 1 = 13.3
    解释： 在运算过程中，python会把整数转化成浮点数进行运算

    在交互模式下，上一次打印出来的表达式被赋值给变量 _
    例如：
    tax = 12.5 / 100
    price = 100.50
    print(price * tax)   #12.5625

#3.1列表作为栈使用(后进先出)
    stack = [4, 5, 6]
    stack.append([7, 8])
    stack.pop()
    [7, 8]
    print(stack)
    [4, 5, 6]
    stack.append(7)
    stack.append(8)
    stack.append(9)
    stack.pop()
    9
    stack
    [4, 5, 6, 7, 8] 

#3.2列表作为队列使用（先进先出）
    from _collections import deque
    queue = deque(["12", "56", "78"])
    queue.append('33')
    queue.append('44')
    queue
    deque(['12', '56', '78', '33', '44'])
    queue.popleft()
    '12'
    queue.popleft()
    '56'
    queue
    deque(['78', '33', '44'])

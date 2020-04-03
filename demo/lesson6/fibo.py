# from python.demo.lesson03.fibo import fib, fib2
# print(fib(500))
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
'''
from python.demo.lesson03.fibo import *
print(fib(1000))
'''

'''
from python.demo.lesson03.fibo import fib as fibonaci
fibonaci(1000)
注解
出于效率的考虑，每个模块在每个解释器会话中只被导入一次。因此,
如果你更改了你的模块，则必须重新启动解释器， 或者，如果它只是一个要交互式地测试的模块，
请使用 importlib.reload()，例如 import importlib; importlib.reload(modulename)。 
'''
import django
print(django.get_version())



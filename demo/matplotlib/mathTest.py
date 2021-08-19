import math

import numpy as np
import matplotlib.pyplot as plt

'''
# 定义x、y散点坐标
x = [10, 20, 30, 40, 50, 60, 70, 80]
x = np.array(x)
num = [174, 236, 305, 334, 349, 351, 342, 323]
y = np.array(num)
# 采用三次多项式拟合
f1 = np.polyfit(x, y, 3)
print('f1 is :\n', f1)

p1 = np.poly1d(f1)
print('p1 is :\n', p1)

# 使用yvals=np.polyval(f1, x)拟合y值
yvals = p1(x)
print('yvals is :\n', yvals)

#绘图
plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('polyfitting')
plt.show()
'''
# 第一种方案是给出具体的函数形式(可以是任意的，只要你能写的出来 下面的func就是)，
# 用最小二乘的方式去逼近和拟合，求出函数的各项系数
'''
from scipy.optimize import curve_fit


# 自定义函数 e指数形式
def func(x, a, b, c):
    return a * np.sqrt(x) * (b * np.square(x) + c)


# 定义x、y散点坐标
x = [20, 30, 40, 50, 60, 70]
x = np.array(x)
num = [453, 482, 503, 508, 498, 479]
y = np.array(num)

# 非线性最小二乘法拟合
popt, pcov = curve_fit(func, x, y)
# 获取popt里面是拟合系数
print(popt)
a = popt[0]
b = popt[1]
c = popt[2]
yvals = func(x, a, b, c)  # 拟合y值
print('popt:', popt)
print('系数a:', a)
print('系数b:', b)
print('系数c:', c)
print('系数pcov:', pcov)
print('系数yvals:', yvals)
# 绘图
plot1 = plt.plot(x, y, 's', label='original values')
plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4)  # 指定legend的位置右下角
plt.title('curve_fit')
plt.show()
'''

# 高斯方法拟合
# encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd


# 自定义函数 e指数形式
def func(x, a, u, sig):
    return a * (np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig)) * (431 + (4750 / x))


# 定义x、y散点坐标
x = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135]
x = np.array(x)
# x = np.array(range(20))
print('x is :\n', x)
num = [536, 529, 522, 516, 511, 506, 502, 498, 494, 490, 487, 484, 481, 478, 475, 472, 470, 467, 465, 463]
y = np.array(num)
print('y is :\n', y)

popt, pcov = curve_fit(func, x, y, p0=[3.1, 4.2, 3.3])
# 获取popt里面是拟合系数
a = popt[0]
u = popt[1]
sig = popt[2]

yvals = func(x, a, u, sig)  # 拟合y值
print(u'系数a:', a)
print(u'系数u:', u)
print(u'系数sig:', sig)

# 绘图
plot1 = plt.plot(x, y, 's', label='original values')
plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4)  # 指定legend的位置右下角
plt.title('curve_fit')
plt.show()

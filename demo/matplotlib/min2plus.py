'''
最小二乘法（又称最小平方法）是一种数学优化技术。它通过最小化误差的平方和寻找数据的最佳函数匹配。
利用最小二乘法可以简便地求得未知的数据，并使得这些求得的数据与实际数据之间误差的平方和为最小。
最小二乘法还可用于曲线拟合。其他一些优化问题也可通过最小化能量或最大化熵用最小二乘法来表达。
所谓最小二乘法，即通过对数据进行拟合，使得拟合值与样本值的方差最小。
'''
# 说明：利用最小二乘法拟合函数y=sin(2πx)
import numpy as np
import scipy as sp
import pylab as pl
from scipy.optimize import leastsq  # 引入最小二乘法

n = 9  # 多项式的次数


# 目标函数y=sin(2πx)
def real_func(x):
    return np.sin(2 * np.pi * x)


# 多项式函数(拟合函数， 也就是h(x))
def fit_func(p, x):
    f = np.poly1d(p)
    return f(x)


# 残差函数
def residuals_func(p, y, x):
    ret = fit_func(p, x) - y
    return ret


# 随机选取9个数作为x（0-9之间）
x = np.linspace(0, 1, 9)

# 画点时需要的连续点
x_points = np.linspace(0, 1, 10000)

# 目标函数
y0 = real_func(x)

# 添加正态分布噪声后的函数
y1 = [np.random.normal(0, 0.1) + y for y in y0]

# 随机初始化多项式参数
p_init = np.random.randn(n)

plsq = leastsq(residuals_func, p_init, args=(y1, x))

# 输出拟合参数
print('Fitting Parameters: ', plsq[0])

# 绘制y=sin(2πx)
pl.plot(x_points, real_func(x_points), color='red')

# 绘制拟合函数
pl.plot(x_points, fit_func(plsq[0], x_points))

# 绘制随机产生的点
pl.plot(x, y1, 'bo')

pl.legend
pl.show()

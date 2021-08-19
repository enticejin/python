'''
import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return x ** 2 + 1


def f_fit(x, y_fit):
    a, b, c = y_fit.tolist()
    print('a=', a)
    print('b=', b)
    print('c=', c)
    return a * x ** 2 + b * x + c


x = np.linspace(-5, 5)
print('x=%s' % x)
y = f(x) + np.random.randn(len(x))  # 加入噪音
y_fit = np.polyfit(x, y, 2)  # 二次多项式拟合
y_show = np.poly1d(y_fit)  # 函数优美的形式
#print(y_show)  # 打印
y1 = f_fit(x, y_fit)
plt.plot(x, f(x), 'r', label='original')
plt.scatter(x, y, c='g', label='before_fitting')  # 散点图
plt.plot(x, y1, 'b--', label='fitting')
plt.title('polyfitting')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()  # 显示标签
plt.show()
'''

'''
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


def f(x):
    return 2 * np.sin(x) + 3


def f_fit(x, a, b):
    return a * np.sin(x) + b


def f_show(x, p_fit):
    a, b = p_fit.tolist()
    return a * np.sin(x) + b


x = np.linspace(-2 * np.pi, 2 * np.pi)
y = f(x) + 0.5 * np.random.randn(len(x))  # 加入了噪音
p_fit, pcov = curve_fit(f_fit, x, y)  # 曲线拟合
print(p_fit)  # 最优参数
print(pcov)  # 最优参数的协方差估计矩阵
y1 = f_show(x, p_fit)
plt.plot(x, f(x), 'r', label='original')
plt.scatter(x, y, c='g', label='before_fitting')  # 散点图
plt.plot(x, y1, 'b--', label='fitting')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
'''

'''
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

plt.close()
fig=plt.figure()
plt.grid(True)
plt.axis([0,10,0,8])

#列出数据
point=[[1,2],[2,3],[3,6],[4,7],[6,5],[7,3],[8,2]]
plt.xlabel("X")
plt.ylabel("Y")

#用于求出矩阵中各点的值
XSum = 0.0
X2Sum = 0.0
X3Sum = 0.0
X4Sum = 0.0
ISum = 0.0
YSum = 0.0
XYSum = 0.0
X2YSum = 0.0


#列出各点的位置
for i in range(0,len(point)):

 xi=point[i][0]
 yi=point[i][1]
 plt.scatter(xi,yi,color="red")
 show_point = "("+ str(xi) +","+ str(yi) + ")"
 plt.text(xi,yi,show_point)

 XSum = XSum+xi
 X2Sum = X2Sum+xi**2
 X3Sum = X3Sum + xi**3
 X4Sum = X4Sum + xi**4
 ISum = ISum+1
 YSum = YSum+yi
 XYSum = XYSum+xi*yi
 X2YSum = X2YSum + xi**2*yi

# 进行矩阵运算
# _mat1 设为 mat1 的逆矩阵
m1=[[ISum,XSum, X2Sum],[XSum, X2Sum, X3Sum],[X2Sum, X3Sum, X4Sum]]
mat1 = np.matrix(m1)
m2=[[YSum], [XYSum], [X2YSum]]
mat2 = np.matrix(m2)
_mat1 =mat1.getI()
mat3 = _mat1*mat2

# 用list来提取矩阵数据
m3=mat3.tolist()
a = m3[0][0]
b = m3[1][0]
c = m3[2][0]
# 绘制回归线
x = np.linspace(0,10)
y = a + b*x + c*x**2
plt.plot(x,y)
show_line = "y="+str(a)+"+("+str(b)+"x)"+"+("+str(c)+"x2)";
plt.title(show_line)
plt.show()

'''

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.stats import norm
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

''''' 数据生成 '''
x = np.arange(0, 1, 0.002)
y = norm.rvs(0, size=500, scale=0.1)
y = y + x ** 2

''''' 均方误差根 '''


def rmse(y_test, y):
    return sp.sqrt(sp.mean((y_test - y) ** 2))


''''' 与均值相比的优秀程度，介于[0~1]。0表示不如均值。1表示完美预测.这个版本的实现是参考scikit-learn官网文档 '''


def R2(y_test, y_true):
    return 1 - ((y_test - y_true) ** 2).sum() / ((y_true - y_true.mean()) ** 2).sum()


''''' 这是Conway&White《机器学习使用案例解析》里的版本 '''


def R22(y_test, y_true):
    y_mean = np.array(y_true)
    y_mean[:] = y_mean.mean()
    return 1 - rmse(y_test, y_true) / rmse(y_mean, y_true)


plt.scatter(x, y, s=5)
degree = [1, 2, 100]
y_test = []
y_test = np.array(y_test)

for d in degree:
    clf = Pipeline([('poly', PolynomialFeatures(degree=d)),
                    ('linear', LinearRegression(fit_intercept=False))])
    clf.fit(x[:, np.newaxis], y)
    y_test = clf.predict(x[:, np.newaxis])

    print(clf.named_steps['linear'].coef_)
    print('rmse=%.2f, R2=%.2f, R22=%.2f, clf.score=%.2f' %
          (rmse(y_test, y),
           R2(y_test, y),
           R22(y_test, y),
           clf.score(x[:, np.newaxis], y)))

    plt.plot(x, y_test, linewidth=2)

plt.grid()
plt.legend(['imagin-line', 'pre-line', 'ac-line'], loc='upper left')
plt.show()

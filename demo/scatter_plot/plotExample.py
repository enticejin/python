import numpy as np
import matplotlib.pyplot as plt
import demo.scatter_plot.util.getFileXY as getXy
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# matplotlib画图中中文显示会有问题，需要这两行设置默认字体
filename = "D:/work/pointinfo_solve_py.csv"
xy = getXy.getXY(filename)
xList = xy.get("x_list")
yList = xy.get("y_list")




plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(xmax=20, xmin=-20)
plt.ylim(ymax=20, ymin=-20)
# 画两条（0-9）的坐标轴并设置轴标签x，y

# x1 = np.random.normal(2, 1.2, 300)  # 随机产生300个平均值为2，方差为1.2的浮点数，即第一簇点的x轴坐标
# y1 = np.random.normal(2, 1.2, 300)  # 随机产生300个平均值为2，方差为1.2的浮点数，即第一簇点的y轴坐标
# x2 = np.random.normal(7.5, 1.2, 300)
# y2 = np.random.normal(7.5, 1.2, 300)
colors1 = '#00CED1'  # 点的颜色
colors2 = '#DC143C'
area = np.pi * 4 ** 2  # 点面积
# 画散点图
# plt.scatter(x1, y1, s=area, c=colors1, alpha=0.4, label='类别A')
# plt.scatter(x2, y2, s=area, c=colors2, alpha=0.4, label='类别B')
plt.scatter(xList, yList, s=area, c=colors1, alpha=0.4, label='类别A')
plt.plot([-20, 20], [20, -20], linewidth='1', color='#000000')
plt.legend()
plt.show()
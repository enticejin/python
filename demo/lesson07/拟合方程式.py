import csv
import re

import matplotlib.pyplot as plt
import numpy as np

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# y = np.array([5760, 3600, 1620, 1260, 1080, 900, 1080, 1800, 3060, 4680, 2880, 5040, 4140, 5580, 5040, 4860, 3780,
#    3420, 4860, 3780, 4860, 5220, 4860, 3600])
filename = "D:/work/pointinfo_solve_py.csv"
list1 = []
x = []
y = []
i = 0
with open(filename, 'r') as file:
    reader = csv.DictReader(file)
    column = [row['test'] for row in reader]
    for element in column:
        x.append(float(re.split("\\|", column[i])[0]))
        y.append(float(re.split("\\|", column[i])[1]))
        i =i+1;

z1 = np.polyfit(x, y, 2) # 用2次多项式拟合
p1 = np.poly1d(z1)
print(p1) # 在屏幕上打印拟合多项式
yvals=p1(x) # 也可以使用yvals=np.polyval(z1,x)
plot1=plt.plot(x, y, '.',label='original values')
plot2=plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4) # 指定legend的位置,读者可以自己help它的用法
plt.title('polyfitting')
plt.show()
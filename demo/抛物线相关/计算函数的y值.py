import csv
import math
import re

filename = "D:/work/pointinfo_solve_py.csv"
list1 = []
x_list = []
y_list = []
i = 0
with open(filename, 'r') as file:
    reader = csv.DictReader(file)
    column = [row['test'] for row in reader]
    for element in column:
        x_list.append(re.split("\\|", column[i])[0])
        y_list.append(re.split("\\|", column[i])[1])
        i = i + 1;
a = float(-0.03275)
b = float(-0.1466)
x = float(x_list[0])
y = float(y_list[0])
c = float(-0.8099)


def judge(xx):
    return math.sqrt((xx - x) * (xx - x) + (a * xx * xx + b * xx + c - y) * (a * xx * xx + b * xx + c - y))


def func(left=-20, r=20):
    while r - left >= 0.00001:
        mid = (left + r) / 2
        midd = (mid + r) / 2
        if judge(mid) <= judge(midd):
            r = midd
            return r
        else:
            left = mid
            return left
        # print("点(", x, " , ", y, ")到抛物线的距离是", judge(left))


print("函数返回值是： ", func())

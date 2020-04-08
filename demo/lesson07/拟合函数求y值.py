import csv
import re


def functionX(xp):
    a = -0.03275
    b = - 0.1466
    c = -0.8099
    return xp * xp * a + b * xp + c


def functionY(yp):
    a = -0.03275
    b = - 0.1466
    c = -0.8099
    if a < 0:
        # return -(((b ** 2 + 4 * a * yp - 4 * a * c) / (4 * a ** 2)) ** 0.5)
        return (((b ** 2 + 4 * a * yp - 4 * a * c) ** 0.5) - b) / (a * 2)
    else:
        #return ((b ** 2 + 4 * a * yp - 4 * a * c) / (4 * a ** 2)) ** 0.5
        return (((b ** 2 + 4 * a * yp - 4 * a * c) ** 0.5) - b) / (a * 2)


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
        print(x_list[i], "函数对应的Y值：", functionX(float(x_list[i])), "----实际y值： ", y_list[i])
        print("---------------------------------------------------------------------------------------------")
        print(y_list[i], "函数对应的X值：", functionY(float(y_list[i])), "----实际X值： ", x_list[i])
        i = i + 1

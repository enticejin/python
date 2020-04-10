import csv
import re
import matplotlib.pyplot as plt

def functionX(xp):
    a = -0.03275
    b = - 0.1466
    c = -0.8099
    return xp * xp * a + b * xp + c



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
        list1.append(functionX(float(x_list[i])))
        print(x_list[i], "函数对应的Y值：", functionX(float(x_list[i])), "----实际y值： ", y_list[i])
        i = i + 1

plt.scatter(x_list, list1)
plt.show()
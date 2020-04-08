# coding: utf-8
import csv
import re

import matplotlib.pyplot as plt
import numpy as np
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
        i =i+1;
x = np.arange(-20,20)
y = x ** 2 * (-0.03275) - 0.1466 * x - 0.8099

plt.plot(x,y)
plt.show()

import csv
import matplotlib.pyplot as plt
import re
f = open(R"D:\work\pointinfo_solve.csv")
#f = open("D:/work/pointinfo_solve.csv")
#print(f.read())

filename = "D:/work/pointinfo_solve.csv"
list1 = []
x_list = []
y_list = []
i = 0
with open(filename, 'r') as file:
    reader = csv.DictReader(file)
    column = [row['-11.54177605817667|-3.553084689684635|1.0'] for row in reader]
    for element in column:
        x_list.append(re.split("\\|", column[i])[0])
        y_list.append(re.split("\\|", column[i])[1])
        i =i+1;
print(x_list)
print(y_list)
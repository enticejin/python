import csv
import re


def getXY(filename):
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
    return {'x_list': x_list, 'y_list': y_list}

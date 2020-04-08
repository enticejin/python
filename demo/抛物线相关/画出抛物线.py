# coding: utf-8
import csv
import re

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-20,20)
y = x ** 2 * (-0.03275) - 0.1466 * x - 0.8099

plt.plot(x,y)
plt.show()

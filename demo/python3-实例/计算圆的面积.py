#定义一个方法来计算圆的面积
def findArea(r):
    PI = 3.142
    return PI * r**2
#调用方法
num = float(input(("输入圆的半径： ")))
print("圆的面积为 %.6f" % findArea(num))
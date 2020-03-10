'''
a = float(input('第一条边： '))
b = float(input('第二条边： '))
c = float(input('第三条边： '))

#计算半周长
s = (a + b + c)/2

#计算面积
area = (s * (s-a) *(s - b) * (s - c)) ** 0.5
print('三角形面积为 %0.2f' %area)
'''

def fin(a, b , c):
    s = (a + b + c) / 2
    area = (s * (s-a) * (s - b) * (s - c)) ** 0.5
    return area

print('三角形面积为 %0.2f' %fin(3, 4, 5))
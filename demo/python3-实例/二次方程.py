# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0
import cmath

a = int(input('输入a： '))
b = int(input('输入b： '))
c = int(input('输入c： '))

#计算
d =b**2 - (4*a*c)
#两种求解方式
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('结果为 {0} 和 {1}'.format(sol1,sol2))
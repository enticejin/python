num = float(input('输入一个数字： '))
num_sqrt = num ** 0.5
print(' %0.3f 的平方根为 %0.3f'%(num ,num_sqrt))


# 计算实数和复数平方根
# 导入复数数学模块
import cmath
num = int(input('输入数字： '))
sqrt = cmath.sqrt(num)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num ,sqrt.real,num_sqrt.imag))

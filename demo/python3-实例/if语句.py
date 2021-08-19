'''
num = float(input('输入一个数字：'))
if num > 0:
    print(num, '是正数')
elif num == 0:
    print(num, '是0')
else:
    print(num, '负数')
'''

#内嵌式
'''
num = float(input('输入一个数字：'))
if num >= 0:
    if num == 0:
        print(num, '是0')
    print(num, '是正数')
else:
    print(num, '是负数')
'''

#优化代码
while True:
    try:
        num = float(input('输入一个数字：'))
        if num >= 0:
            if num == 0:
                print(num, '是0')
            print(num, '是正数')
        else:
            print(num, '是负数')
        continue
    except ValueError:
        print('输入无效，需要输入一个数字')
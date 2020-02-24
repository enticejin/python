'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：

程序源代码：
'''
year = int(input('年: \n'))
month = int(input('月: \n'))
day = int(input('日: \n'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    sum1 = months[month - 1]
else:
    print('日期错误')

leap = 0
if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
    leap = 1
if(leap == 1) and (month > 2):
    sum1 += 1
print('这是今年的第 %d 天' % sum1)
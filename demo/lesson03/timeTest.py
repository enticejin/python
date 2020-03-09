'''
import  time
time_time = time.time()
print("当前时间是： ", time_time) #当前时间是：  1583746627.278753
'''

'''
import time
localtime = time.localtime(time.time())
print("当前的时间的：",localtime);#当前的时间的： time.struct_time(tm_year=2020, tm_mon=3, tm_mday=9, tm_hour=17, tm_min=39, tm_sec=24, tm_wday=0, tm_yday=69, tm_isdst=0)

'''

'''
import time
localtime = time.asctime(time.localtime(time.time()))
print("本地时间：", localtime)
'''

#获取末月的日历
'''
import calendar

month = calendar.month(2020, 3)
print("以下是2020年三月份的日历")
print(month)
'''
'''
以下是2020年三月份的日历
     March 2020
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
'''



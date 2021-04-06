'''
from time import ctime, sleep

#单线程
def music(func):
    for i in range(2):
        print("I was listening to %s. %s" %(func,ctime()))
        sleep(1)


def movie(func):
    for i in range(2):
        print("我在看电影, %s! 电影名字是 %s "%(ctime(), func))
        sleep(5)


if __name__ == '__main__':
    music('nothing on you!')
    movie('战狼2')
    print("结束： %s" % ctime())
'''
# 多线程
# coding=utf-8
import threading
from time import ctime, sleep


def music(name):
    for i in range(2):
        print('我在听音乐！%s。 %s' % (name, ctime()))
        sleep(1)


def movie(name):
    for i in range(2):
        print('我在看电影！%s, %s' % (name, ctime()))
        sleep(5)

threads = []
t1 = threading.Thread(target=music('nothing on you'))
threads.append(t1)

t2 = threading.Thread(target=movie('Titannic'))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()
        
    print('时间到了该睡觉了！')

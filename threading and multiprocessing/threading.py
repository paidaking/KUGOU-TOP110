import time, threading

def coding():
    for x in range(3):
        print('正在写代码%s' % threading.current_thread()) # 查看当前线程的名字
        time.sleep(1)

def drawing():
    for x in range(3):
        print('正在画图%s' % threading.current_thread())
        time.sleep(1)

def main():
    t1 = threading.Thread(target=coding)  # Thread类
    t2 = threading.Thread(target=drawing)

    t1.start()
    t2.start()

    # print(threading.enumerate()) # 查看线程数

if __name__ == '__main__':
    main()


# 继承自threading.Thread类：

import threading
import time

class CodingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('正在写代码%s' % threading.current_thread()) # 查看当前线程的名字
            time.sleep(1)

class DrawingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('正在画图%s' % threading.current_thread()) # 查看当前线程的名字
            time.sleep(1)

def main():
    t1 = CodingThread()
    t2 = DrawingThread()

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()


# 多线程共享全局变量的问题：

import threading

VALUE = 0

glock = threading.Lock() # 锁

def add_value():
    global VALUE
    glock.acquire() #获取/上锁
    for x in range(1000000):
        VALUE += 1
    glock.release() #释放/解锁
    print('value: %d' % VALUE)

def main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()

if __name__ == '__main__':
    main()


# Lock版本生产者和消费者模式：

import threading
import random, time

gMoney = 100
gLock = threading.Lock()
gTotalTimes = 10
gTimes = 0

class Producer(threading.Thread):
    def run(self):
        global gMoney, gTimes
        while True:
            money = random.randint(100,1000)
            gLock.acquire()
            if gTimes >= gTotalTimes:
                gLock.release()
                break
            gMoney += money
            print('%s生产了%d元钱，剩余%d元钱' % (threading.current_thread(),money,gMoney))
            gTimes += 1
            gLock.release()
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100,1000)
            gLock.acquire()
            if gMoney >= money:
                gMoney -= money
                print('%s消费者消费了%d元钱，剩余%d元钱' % (threading.current_thread(),money,gMoney))
            else:
                if gTimes >= gTotalTimes:
                    gLock.release()
                    break
                print('%s消费者准备消费%d元钱，剩余%d元钱，不足！！！' % (threading.current_thread(),money,gMoney))

            gLock.release()
            time.sleep(0.5)

def main():
    for x in range(3):
        t = Consumer(name='消费者线程%d' % x)
        t.start()

    for x in range(5):
        t = Producer(name='生产者线程%d' % x)
        t.start()

if __name__ == '__main__':
    main()


# Condition版的生产者与消费者模式：

import threading
import random, time

gMoney = 100
gCondition = threading.Condition()
gTotalTimes = 10
gTimes = 0

class Producer(threading.Thread):
    def run(self):
        global gMoney, gTimes
        while True:
            money = random.randint(100,1000)
            gCondition.acquire()
            if gTimes >= gTotalTimes:
                gCondition.release()
                break
            gMoney += money
            print('%s生产了%d元钱，剩余%d元钱' % (threading.current_thread(),money,gMoney))
            gTimes += 1
            gCondition.notify_all()
            gCondition.release()
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100,1000)
            gCondition.acquire()
            while gMoney < money:
                if gTimes >= gTotalTimes:
                    gCondition.release()
                    return
                print('%s准备消费%d元钱，剩余%d元钱，不足！'% (threading.current_thread(),money,gMoney))
                gCondition.wait()
            gMoney -= money
            print('%s消费了%d元钱，剩余%d元钱' % (threading.current_thread(),money,gMoney))
            gCondition.release()
            time.sleep(0.5)

def main():
    for x in range(3):
        t = Consumer(name='消费者线程%d' % x)
        t.start()

    for x in range(5):
        t = Producer(name='生产者线程%d' % x)
        t.start()

if __name__ == '__main__':
    main()


# Queue线程安全队列

from queue import Queue
import threading,time

def set_value(q):
    index = 0
    while True:
        q.put(index)
        index += 1
        time.sleep(1)

def get_value(q):
    while True:
        print(q.get())

def main():
    q = Queue(4)
    t1 = threading.Thread(target=set_value,args=[q])
    t2 = threading.Thread(target=get_value,args=[q]) # 参数用列表或者元组传进去

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()


# GIL全局解释器锁：

cpython 是个伪线程（在多核cpu中只能利用一核，不能利用多核），同一时间只有一个线程在执行，为了保证同一时间只有一个线程在执行，
在cpython解释器中有一个东西叫全能解释器锁（GIL），因为cpython解释器的线程管理不是安全的。

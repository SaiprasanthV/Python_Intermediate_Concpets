''' 
This module is to understand how to synchronize the threads using Lock.
Lock prevents other threads from accessing the resource until lock is released.
Notice the diffence when you run with and without LOCK.

'''

import threading
import time

num = 8192
lock = threading.Lock()


def double():
    global num, lock
    lock.acquire()
    while(num < 9000):
        num = num*2
        print(num)
        time.sleep(1)
    lock.release()
    print('Reached Maximum')


def half():
    global num, lock
    lock.acquire()
    while(num > 1):
        num = num/2
        print(num)
        time.sleep(1)
    lock.release()
    print('Reached Minimum')


t1 = threading.Thread(target=half)
t1.start()
t2 = threading.Thread(target=double)
t2.start()

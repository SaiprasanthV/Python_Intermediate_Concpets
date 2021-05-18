''' 
This module is to understand how to synchronize the threads using Semaphore. 
Semaphore restricts the maximum number of access allowed.

'''
import threading
import time

semaphore = threading.BoundedSemaphore(value=5)


def access(thread_num):
    print(f'{thread_num} is trying to access')
    semaphore.acquire()
    print(f'{thread_num} is granted  access')
    time.sleep(10)
    print(f'{thread_num} is now releasing')
    semaphore.release()


for i in range(1, 11):
    t = threading.Thread(target=access, args=(i,))
    t.start()
    time.sleep(1)

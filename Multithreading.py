''' 
This module is to understand how a Multithreading works and how to prevent the main thread to run before custom thread ends.
Notice the diffence when you run with and without JOIN.

'''

import threading


def function_1():
    for i in range(50):
        print(i, 'one')


def function_2():
    for i in range(50):
        print(i, 'two')


t1 = threading.Thread(target=function_1)
t1.start()
# t1.join()

t2 = threading.Thread(target=function_2)
t2.start()
# t2.join()
print('Finished')

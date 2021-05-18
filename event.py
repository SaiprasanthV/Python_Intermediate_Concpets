''' 
This module is to understand how the event works and how to trigger the event. 
Semaphore restricts the maximum number of access allowed.

'''

import threading

event = threading.Event()


def function():
    print('My function is waiting for Trigger ............')
    event.wait()
    print('Task ABC is finished')


t = threading.Thread(target=function)
t.start()


reply = input('Do you want to trigger the Event? y/n :')
if reply == 'y':
    event.set()

''' 
This module is to understand how a class can be created

'''


class Person:
    count = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.count += 1

    def __del__(self):
        Person.count -= 1

    def __str__(self):
        return (f'Name:{self.name}, Age:{self.age}, Height:{self.height}')


person_1 = Person('Sai', 21, 175)
print('Person 1 -> ', person_1)
print('Person Count after adding 1st person:', Person.count)

person_2 = Person('Parthi', 23, 170)
print('Person 2 -> ', person_2)
print('Person Count after adding 2nd person:', Person.count)

del person_2
print('Person Count after deleting 2nd person:', Person.count)

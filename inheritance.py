''' 
This module is to understand how to inherit a class and to override the parent class

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


class Worker(Person):

    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def __str__(self):
        return (super(Worker, self).__str__() + f' Salary: {self.salary}')

    def check_year_salary(self):
        return self.salary*12


worker_1 = Worker('Sai', 21, 175, 30000)
print('Worker 1 -> ', worker_1)
print('Person Count after adding 1st Worker:', Worker.count)
print('Salary in LPA:', worker_1.check_year_salary())

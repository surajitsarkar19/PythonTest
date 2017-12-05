class Person:

    def __init__(self, name, age = -1):
        self.name = name
        self.age = age

    def say_hi(self):
        print('Hello, my name is', self.name)

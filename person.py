class Person:

    msg = "discaoo" #class variable

    def __init__(self, name, age = -1):
        self.name = name #instance variable
        self.age = age

    def say_hi(self):
        print('Hello, my name is', self.name)

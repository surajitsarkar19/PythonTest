# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#
# Hints:
# Use __init__ method to construct some parameters

class ConsoleInput:
    '''Read and get console input'''

    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = raw_input("Enter some value")

    def printString(self):
        print(self.str.upper())


consoleInput = ConsoleInput()
consoleInput.getString()
consoleInput.printString()
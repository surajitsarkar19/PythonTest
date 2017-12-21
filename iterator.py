class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    # __next__() is for Python3
    # next() is for python 2
    def next(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


#generator is a function
def PowTwoGen(max=0):
    '''Same functionality using generator'''
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

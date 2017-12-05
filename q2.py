# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        print "{}*fact({})".format(n, n - 1)
        return n * fact(n - 1)


def factTail(n, res):
    if n == 0:
        return res
    else:
        # print "factTail({}) = {}".format(n, res)
        return factTail(n - 1, res * n)


number = int(input("Enter your number:"));
print "Factorial of {} is {}".format(number, factTail(number, 1))

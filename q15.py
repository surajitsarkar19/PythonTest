# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def splitString(source, splitlist):
    output = []  # output list of cleaned words
    atsplit = True
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)  # append new word after split
                atsplit = False
            else:
                output[-1] = output[-1] + char  # continue copying characters until next split
    return output


a = input("Enter value of a :")

expression = "a+aa+aaa+aaaa"

value = 0

for x in splitString(expression, "+"):
    s = x.replace("a", str(a))
    val = int(s)
    value += val

print(value)

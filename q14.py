# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


input = raw_input("Enter the text :")

upper = []
lower = []

for str in input:
    ascii = ord(str)
    if ascii>64 and ascii<91:
        upper.append(str)
    elif ascii>96 and ascii<123:
        lower.append(str)
print("UPPER CASE", len(upper))
print("LOWER CASE", len(lower))
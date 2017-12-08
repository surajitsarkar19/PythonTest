# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

input = raw_input("Enter the text :")

letters = []
digits = []

for str in input:
    ascii = ord(str)
    if ascii>47 and ascii<58:
        digits.append(str)
    elif ascii>64 and ascii<91:
        letters.append(str)
    elif ascii>96 and ascii<123:
        letters.append(str)
print("LETTERS", len(letters))
print("DIGITS", len(digits))
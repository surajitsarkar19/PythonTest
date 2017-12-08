# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check
# whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated
# sequence. Example: 0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input by console.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

input  = raw_input("Enter comma seperated binary sequence :")

xx = [x for x in input.split(",")]
output = []
for num in xx:
    decimalVal = int(num,2)
    if decimalVal%5 == 0:
        output.append(num)
print(output)
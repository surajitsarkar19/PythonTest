# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the
#  number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def isEven(num):
    digits = []
    while num > 9:
        rem = num % 10
        digits.append(rem)
        num = num // 10
    else:
        digits.append(num)

    count = 0;
    for i in digits:
        if i % 2 == 0:
            count += 1
    return count == len(digits)


output = []
for n in range(1000, 3001):
    if isEven(n):
        output.append(str(n))

print(output)
print(",".join(output))

# Problem 8
#
# Find the greatest product of five consecutive digits 
# in the 1000-digit number.
#

import operator


# Get 1000 digit number in an list
number = []
for line in open('in.txt'):
    number.extend([int(x) for x in line.rstrip()])

# Calculate the greatest product of 5 consecutive digits
largest = 0
for i in range(996):
    product = reduce(operator.mul, number[i : i+5], 1)
    if (product > largest):
        largest = product

print largest


 

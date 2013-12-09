# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#     a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

def isPythagoreanTriplet(a, b):
    c = math.sqrt(a*a + b*b)
    return math.floor(c) == c

# Get all pythagorean triplets for 1 < a < b < 1000
pTriplets = [(a, b, int(math.sqrt(a*a + b*b))) 
             for a in range(1, 500) 
             for b in range(a+1, 500)
             if isPythagoreanTriplet(a, b)]

# Get triplet whose sum is 1000
a, b, c = next(pTriplet for pTriplet in pTriplets if sum(pTriplet) == 1000)
print a * b * c 


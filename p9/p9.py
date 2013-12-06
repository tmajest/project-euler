# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#     a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

def isPerfectSquare(n):
    sqrt = math.sqrt(n)
    return math.floor(sqrt) == sqrt

def solve():
    for a in range(1, 500):
        for b in range(a+1, 500):
            c2 = a*a + b*b
            if isPerfectSquare(c2):
                c = int(math.sqrt(c2))
                if (a + b + int(c) == 1000):
                    return (a, b, int(c))

a, b, c = solve()
print a * b * c


    
                



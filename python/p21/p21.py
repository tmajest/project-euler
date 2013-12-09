# http://projecteuler.net/problem=21

import math


def divisors(n):
    """ Returns the divisors of n that are less than n """
    dvs = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            dvs.append(i)
            j = n / i
            if j != i:
                dvs.append(j)

    dvs.remove(n)
    return dvs

def d(n):
    """ Finds the sum of the divisors less than n """
    return sum(divisors(n))


# Compute the list of amicable numbers less than 10,000 and print their sum
amicable_nums = set()
for a in range(2, 10000):
    b = d(a)
    if d(b) == a and a != b:
        amicable_nums.add(a)
        amicable_nums.add(b)

print sum(amicable_nums)

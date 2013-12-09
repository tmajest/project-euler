# http://projecteuler.net/problem=12

import itertools
import math


def triangle_number(n):
    """ Returns the nth triangle number """
    return n * (n + 1) / 2

def divisors(n):
    """ Find the divisors (and their n / divisor complement) for the
        numbers up to sqrt(n) + 1 """
    d = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            d.append(i)
            d.append(n / i)
    return set(d)


# Find the first triangle number with more than 500 divisors

for i in itertools.count(1):
    t = triangle_number(i)
    if len(divisors(t)) > 500:
        print t
        break


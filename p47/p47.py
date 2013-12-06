# Project euler problem 47
# http://projecteuler.net/problem=47

import prime_tools

a, b, c, d = [prime_tools.prime_factors(n) for n in range(2, 6)]

for i in xrange(3, 1000000):
    a, b, c, d = b, c, d, prime_tools.prime_factors(i + 3)

    # Check that each number has only 4 prime factors and that they share
    # no factors in common (set intersection of their factors is empty)
    if 4 == len(a) == len(b) == len(c) == len(d) and len(a & b & c) == 0:
        print i
        break

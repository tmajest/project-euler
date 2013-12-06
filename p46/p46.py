# Project euler problem 46 
# http://projecteuler.net/problem=46

import prime_tools

def goldbach_conjecture(n, primes):
    """ Returns true if the number can be expressed as the sum of a prime
        and twice a square """
    for prime in primes:
        for i in xrange(1, n):
            total = prime + 2 * i * i
            if total == n:
                return True
            elif total > n:
                break

    return False

primes = prime_tools.primes_up_to(10000)
composites = prime_tools.composites_up_to(10000)

for c in composites:
    if c % 2 == 1 and c > 1 and not goldbach_conjecture(c, primes):
        print c
        break

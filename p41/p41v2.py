# Project euler problem 41
# http://projecteuler.net/problem=41

import prime_tools

def is_pandigital(num):
    num_str = str(num)
    return sorted(map(int, num_str)) == range(1, len(num_str) + 1)

primes = reversed(prime_tools.primes_up_to(10000000))
print next(prime for prime in primes if is_pandigital(prime))

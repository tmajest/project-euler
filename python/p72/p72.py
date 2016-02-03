# https://projecteuler.net/problem=72

import prime_tools
import math

def euler_phi(n, primes):
    """
    https://en.wikipedia.org/wiki/Euler%27s_totient_function
    """
    product = n
    factors = prime_tools.prime_factors(n, primes)
    for factor in factors:
        product /= factor
        product *= (factor - 1)

    return int(product)




limit = 1000000
primes = prime_tools.primes_up_to(int(limit ** 0.5))
result = sum(euler_phi(i, primes) for i in range(2, limit + 1))
print(result)


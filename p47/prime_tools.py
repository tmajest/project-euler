# Contains prime generator functions

import math
import collections

def primes_up_to(num):
    """ Prime sieve: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Implementation """
    primes = [True for i in xrange(num + 1)]
    primes[0] = False
    primes[1] = False

    for i in xrange(2, int(math.sqrt(num) + 1)):
        if primes[i]:
            for j in xrange(i * i, num + 1, i):
                primes[j] = False

    return [pos for pos, is_prime in enumerate(primes) if is_prime]

def prime_factors(num):
    """ 
    Kind of hacky implementation of prime factorization.
    Returns a set of tuples (a, b) represeting the factor a to the bth power
    """
    factors = collections.defaultdict(int)
    curr_factor = 2

    while num > 1:
        if num % curr_factor == 0:
            factors[curr_factor] += 1
            num /= curr_factor
        else:
            curr_factor += 1 if curr_factor == 2 else 2

    return set(factors.iteritems())

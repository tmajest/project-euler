# Contains prime generator functions

import math

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

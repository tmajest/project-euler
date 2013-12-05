# Project euler problem 41
# http://projecteuler.net/problem=41

import math

def primes_up_to(num):
    """ Prime sieve: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Implementation """
    primes = [True for i in xrange(num)]
    primes[0] = False
    primes[1] = False

    for i in xrange(2, int(math.sqrt(num) + 1)):
        if primes[i]:
            for j in xrange(i * i, num, i):
                primes[j] = False

    return [pos for pos, is_prime in enumerate(primes) if is_prime]

def is_pandigital(num):
    digits = map(int, str(num))
    used_digits = set()
    n = len(digits)

    for digit in digits:
        if digit == 0 or digit > n or digit in used_digits:
            return False
        used_digits.add(digit)

    return True

primes = reversed(primes_up_to(10000000))
print next(prime for prime in primes if is_pandigital(prime))


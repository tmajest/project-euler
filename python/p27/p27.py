# http://projecteuler.net/problem=27

import itertools

def primes_up_to(n):
    """ Generate all the primes up to n using prime sieve. """
    sieve = [True for i in range(n)]
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False

    return sieve

def num_primes_from_quadratic(a, b, sieve):
    """ Using the quadratic equation, (n ** 2) + an + b, return the number
        of consecutive primes the equation produces, starting with n = 0. """
    for n in itertools.count():
        if not sieve[(n ** 2) + (a * n) + b]:
            return n
                

# Calculate the values of a and b that generate the greatest consecutive
# number of primes for the equation n**2 + an + b:

max_num_primes = 0
maxA = maxB = 0
sieve = primes_up_to(1000000)

for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        curr_num_primes = num_primes_from_quadratic(a, b, sieve)
        if curr_num_primes > max_num_primes:
            max_num_primes, maxA, maxB = curr_num_primes, a, b

print maxA * maxB

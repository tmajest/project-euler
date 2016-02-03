# Contains prime generator functions

import math
def primes_up_to(num):
    """ Prime sieve: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Implementation """
    primes = [True for i in range(num + 1)]
    primes[0] = False
    primes[1] = False

    for i in range(2, int(math.sqrt(num) + 1)):
        if primes[i]:
            for j in range(i * i, num + 1, i):
                primes[j] = False

    return [pos for pos, is_prime in enumerate(primes) if is_prime]

def prime_factors(n, primes):
    """ 
    Compute primes up to sqrt(num) and find which nums divide evenly
    http://en.wikipedia.org/wiki/Trial_division 
    """
    prime_factors = []
    for p in primes:
        if p*p > n: 
            break
        while n % p == 0:
            prime_factors.append(p)
            n //= p

    if n > 1: 
        prime_factors.append(n)

    return set(prime_factors)



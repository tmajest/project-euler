# http://projecteuler.net/problem=35

import math

def primesUpTo(n):
    n = 2000000
    a = [True for i in range(n)]
    a[0], a[1] = False, False

    # Perform sieve
    for i in range(2, int(math.sqrt(n)) + 1):
        if a[i]:
            for j in range(i*i, n, i):
                a[j] = False

    return {i for i, isPrime in enumerate(a) if isPrime}

def rotations(n):
    s = str(n)
    for i in range(len(s)):
        yield s
        s = s[1:] + s[0]

def isCircularPrime(n, primes):
    for r in rotations(n):
        if int(r) not in primes:
            return False
    return True


primes = primesUpTo(1000000)
print len([prime for prime in primes if isCircularPrime(prime, primes)])

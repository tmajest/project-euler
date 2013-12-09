# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
#
# Prime sieve from 
# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Implementation

import math

n = 2000000
a = [True for i in range(n)]
a[1] = False

# Perform sieve
for i in range(2, int(math.sqrt(n)) + 1):
    if a[i]:
        for j in range(i*i, n, i):
            a[j] = False

# Get sum of primes up to 2000000
print sum([i for i, isPrime in enumerate(a) if isPrime])



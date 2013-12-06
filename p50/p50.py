# Project euler problem 50
# http://projecteuler.net/problem=50

import prime_tools

primes = prime_tools.primes_up_to(1000000)
prime_set = set(primes)
max_prime_sum = (0, 0)

for i in xrange(len(primes)):
    total = 0

    for j in xrange(i, len(primes)):
        prime = primes[j]
        total += prime

        if total > primes[-1]:
            break
        elif total in prime_set:
            length = j - i + 1
            max_prime_sum = max(max_prime_sum, (length, total))

print max_prime_sum[1]

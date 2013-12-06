# http://projecteuler.net/problem=32

import itertools

def isPandigital(n):
    return ''.join(sorted(n)) == '123456789'

def get_divisors(n):
    """ Return the divisors of n """
    return [(i, n / i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0]

results = set()
for pandigital in itertools.permutations('123456789'):
    for divisor1, divisor2 in get_divisors(int(''.join(pandigital))):
        if isPandigital('{0}{1}{2}'.format(divisor1, divisor2, divisor1 * divisor2)):
            results.add(divisor1 * divisor2)
            print divisor1 * divisor2

print sum(results)

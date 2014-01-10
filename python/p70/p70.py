# http://projecteuler.net/problem=69
import prime_tools

def product(nums):
    return reduce(lambda total, n: total * n, nums, 1)

def totient_function(n, primes):
    """ 
    Calculates the number of integers less than n that are relatively prime to n.
    See  http://en.wikipedia.org/wiki/Euler's_totient_function  for details
    """
    factors = prime_tools.prime_factors(n, primes)
    return int(round(n * product(1 - (1.0 / factor) for factor in factors)))


def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))


MAX_NUM = 10 ** 7
primes = prime_tools.primes_up_to(int(MAX_NUM ** 0.5) + 1)

n, min_ratio = 1, 10000
for i in range(2, MAX_NUM):
    totient = totient_function(i, primes)
    ratio = i * 1.0 / totient

    if ratio < min_ratio and is_permutation(i, totient):
        n, min_ratio = i, ratio

print n

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
    return int(n * product(1 - 1.0 / factor for factor in factors))


primes = prime_tools.primes_up_to(int(1000000 ** 0.5) + 1)
print max((i * 1.0 / totient_function(i, primes), i) for i in xrange(2, 1000001))[1]

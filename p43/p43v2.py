# Project euler problem 43
# http://projecteuler.net/problem=43
#
# Solution is slower but with fewer lines.  Doesn't have the benefit of
# short circuiting if one of the substrings is not divisible by its prime

import itertools

def has_weird_property(num_str):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    return all(int(num_str[i+1:i+4]) % divisors[i] == 0 for i in xrange(7))

pandigitals = [''.join(p) for p in itertools.permutations('0123456789')]
print sum(int(p) for p in pandigitals if has_weird_property(p))

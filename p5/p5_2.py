# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all 
# of the numbers from 1 to 20?

import collections

def getPrimeFactors(n):
    num = n
    factors = collections.defaultdict(int)
    factor = 2
    while factor <= n:
        if num % factor == 0:
            factors[factor] += 1
            num /= factor
        else:
            factor += 1 
    
    return factors


total_factors = dict()

# For each prime factorization of the numbers 1-20, find the count of each
# factor.  Record the greatest count of each factor.  The product of these
# factors is the smallest value divisible by the numbers 1 - 20.
for i in range(1, 21):
    factors = getPrimeFactors(i)
    for factor, count in factors.iteritems():
        if not total_factors.has_key(factor) or count > total_factors[factor]:
            total_factors[factor] = count

product = 1
for factor, count in total_factors.iteritems():
    product *= factor ** count

print product

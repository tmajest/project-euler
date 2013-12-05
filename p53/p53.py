# Project euler problem 53
# http://projecteuler.net/problem=53
import operator

def factorial(n):
    return 1 if n == 0 else reduce(operator.mul, range(1, n+1), 1)

def choose(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

print len([1 for n in range(1, 101) for r in range(n) if choose(n, r) > 1000000])

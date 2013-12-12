# http://projecteuler.net/problem=57
from fractions import Fraction
import itertools

def square_root_convergents(num_iterations=1):
    num = Fraction(2)
    for i in xrange(num_iterations):
        curr_ans = 1 + (1 / num)
        yield 1 + (1 / num)
        num = (1 / num) + 2

count = 0
for fraction in square_root_convergents(num_iterations=1000):
    numerator, denominator = fraction.numerator, fraction.denominator
    count += 1 if len(str(numerator)) > len(str(denominator)) else 0

print count

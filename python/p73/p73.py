# https://projecteuler.net/problem=73

from fractions import Fraction

def solve(limit):
    fractions = set()
    low = Fraction(1, 3)
    high = Fraction(1, 2)

    for denominator in range(3, limit + 1):
        for numerator in range(denominator // 3, (denominator // 2) + 1):
            fraction = Fraction(numerator, denominator)
            if low < fraction < high:
                fractions.add(fraction)

    return len(fractions)

limit = 12000
print(solve(limit))

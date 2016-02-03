# https://projecteuler.net/problem=65

import itertools
from fractions import Fraction

def convergence_sum(n, sequence):
    first = sequence[0] 
    total = Fraction(first, 1)

    for num in sequence[1:]:
        total = Fraction(1, total) + Fraction(num, 1)

    return total

def e_sequence(limit):
    nums = [2]
    for i in range(1, limit):
        nums.append(1)
        nums.append(i * 2)
        nums.append(1)

    return list(reversed(nums[:limit]))

limit = 100
sequence = e_sequence(limit)
total = convergence_sum(limit, sequence)

print(sum(map(int, str(total.numerator))))

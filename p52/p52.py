# Project euler problem 52
# http://projecteuler.net/problem=52
import itertools

for num in itertools.count(1):
    if len({frozenset(str(num * i)) for i in range(1, 7)}) == 1:
        print num
        break

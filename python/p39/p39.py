# Project euler problem 39
# http://projecteuler.net/problem=39

import collections
import math

def generate_right_triangles(upTo):
    for a in range(1, upTo):
        for b in range(a, upTo):
            c = math.sqrt(a ** 2 + b ** 2)
            if c == math.ceil(c):
                yield (a, b, int(c))

right_triangles = generate_right_triangles(1000)
perimeter_dict = collections.defaultdict(int)

for sides in right_triangles:
    perimeter = sum(sides)
    if perimeter < 1000:
        perimeter_dict[perimeter] += 1

print max(perimeter_dict, key=perimeter_dict.get)

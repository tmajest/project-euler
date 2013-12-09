# Project euler problem 38
# http://projecteuler.net/problem=38

import itertools

def is_pandigital(num_str):
    return sorted(map(int, num_str)) == range(1, len(num_str) + 1)

pandigitals = []
for i in range(1, 10000):
    pandigital_product = [i]
    for j in range(2, 10000):
        pandigital_product.append(i * j)
        pandigital_product_str = ''.join(map(str, pandigital_product))
        if len(pandigital_product_str) < 9:
            continue
        elif len(pandigital_product_str) > 9:
            break
        elif is_pandigital(pandigital_product_str):
            pandigitals.append(int(pandigital_product_str))

print max(pandigitals)

# Project euler problem 43
# http://projecteuler.net/problem=43

import itertools

def has_weird_property(num_str):
    return int(num_str[1:4]) % 2 == 0 and    \
           int(num_str[2:5]) % 3 == 0 and    \
           int(num_str[3:6]) % 5 == 0 and    \
           int(num_str[4:7]) % 7 == 0 and    \
           int(num_str[5:8]) % 11 == 0 and   \
           int(num_str[6:9]) % 13 == 0 and  \
           int(num_str[7:10]) % 17 == 0

pandigitals = [''.join(p) for p in itertools.permutations('0123456789')]
print sum(int(p) for p in pandigitals if has_weird_property(p))

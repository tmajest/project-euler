# http://projecteuler.net/problem=26

import math, itertools

def divide(dividend, divisor, precision=10):
    """ Returns a string representation of the result of the
        division with a certain amount of precision. """
    result = []
    decimal = False

    while len(result) < precision:
        quotient = dividend / divisor
        remainder = dividend % divisor
        result.append(quotient)
        
        if quotient > 0 and remainder == 0:
            break
        elif quotient == 0 and remainder > 0 and not decimal:
            result.append('.')
            decimal = True

        dividend = remainder * 10

    return ''.join(map(str, result))

def cycle_length(string):
    """ Finds a cycle in the string and computes its length """

    # Try to find a cycle starting on each letter in the string
    for i in range(len(string)):
        s = string[i:]

        # Try cycle lengths of 1, 2, ... len/2
        for cycle_len in range(1, int(math.ceil(len(s) / 2.0)) + 1):

            # See if there is a cycle starting at character i
            # of each cycle length
            foundCycle = True
            once = False
            for j in range(len(s) - i - cycle_len):
                once = True
                if s[i + j + cycle_len] != s[i + j % cycle_len]:
                    foundCycle = False
                    break

            if once and foundCycle:
                return cycle_len

    # No cycle found
    return 0


max_cycle, max_i = 1, 1
for i in range(2, 1000):         
    curr_cycle = cycle_length(divide(1, i, 2000))
    if curr_cycle > max_cycle:
        max_cycle, max_i = curr_cycle, i

print max_i






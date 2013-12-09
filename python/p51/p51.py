# http://projecteuler.net/problem=51

import prime_tools
from itertools import combinations


def replace(num, positions, digit):
    """ Replace the digits in the number at the given positions with a new value """
    num_str = str(num)
    return int(''.join(num_str[i] if i not in positions else str(digit) for i in range(len(num_str))))

def num_prime_digit_replacements(num, primes):
    """ 
    Returns the number of primes that can be made by replacing any combination
    of digits in the prime with the same digit
    """
    positions = range(len(str(num)))

    # Try replacing all combinations of positions
    max_prime_count = 0
    for r in range(len(positions) + 1):
        for replace_positions in combinations(positions, r):
            print replace_positions
            new_nums = {replace(num, replace_positions, i) for i in range(10)}
            p = [n for n in new_nums if n in primes]
            print p
            prime_count = len(p)
            max_prime_count = max(max_prime_count, prime_count)

    return max_prime_count


primes = prime_tools.primes_up_to(1000000)
prime_set = set(primes)
#for prime in primes:

print num_prime_digit_replacements(56003, prime_set)



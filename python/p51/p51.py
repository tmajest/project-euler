# http://projecteuler.net/problem=51

import prime_tools
from itertools import combinations


def replace(num, positions, digit):
    """ Replace the digits in the number at the given positions with a new value """
    num_str = str(num)
    return int(''.join(num_str[i] if i not in positions else str(digit) for i in range(len(num_str))))

def get_prime_replacements(num, positions, primes):
    """ 
    Finds the primes that can be generated from a number by replacing digits in 
    the given positions with the same digit 
    
    E.g. Given the number 211 and the positions [1, 2], you can generate the following primes
    by replacing the digit at position 1 and 2 with any of the same digit:
        - 211
        - 233
        - 277
    """
    prime_replacements = set()
    num_str = str(num)

    for digit in range(10):
        new_num = replace(num, positions, digit)

        # Check that we didn't try to create number with a 0 as the leading digit
        if len(str(new_num)) == len(num_str) and new_num in primes:
            prime_replacements.add(new_num)

    return prime_replacements

def get_replacement_positions(num):
    """ 
    Find all the combinations of positions of digits that can be replaced.
    You can only replace digits that share the same value.
    E.g. 56003 will allow you to replace the following positions:
        - *6003
        - 5*003
        - 56*03
        - 56**3
        - 560*3
        - 5600*
    """
    replacement_positions = []
    num_str = str(num)
    for digit in num_str:
        positions = [pos for pos, dig in enumerate(num_str) if digit == dig]
        
        for r in range(len(positions) + 1):
            replacement_positions.extend(combinations(positions, r))

    return replacement_positions


def num_prime_digit_replacements(num, primes):
    """ 
    Returns the number of primes that can be made by replacing any combination
    of digits in the prime with the same digit
    """
    positions = range(len(str(num)))

    # Try replacing all combinations of positions
    max_prime_count = 0
    for replace_positions in get_replacement_positions(num):
        prime_replacements = get_prime_replacements(num, replace_positions, primes)
        max_prime_count = max(max_prime_count, len(prime_replacements))

    return max_prime_count


primes = prime_tools.primes_up_to(1000000)
prime_set = set(primes)

for prime in primes:
    if num_prime_digit_replacements(prime, prime_set) == 8:
        print prime
        break



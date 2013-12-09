# Project euler problem 41
# http://projecteuler.net/problem=41

import prime_tools

def is_pandigital(num):
    digits = map(int, str(num))
    used_digits = set()
    n = len(digits)

    for digit in digits:
        if digit == 0 or digit > n or digit in used_digits:
            return False
        used_digits.add(digit)

    return True

primes = reversed(prime_tools.primes_up_to(10000000))
print next(prime for prime in primes if is_pandigital(prime))


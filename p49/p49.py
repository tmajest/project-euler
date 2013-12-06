# Project euler problem 49
# http://projecteuler.net/problem=49

import prime_tools
import itertools

def solve(): 
    primes = [p for p in prime_tools.primes_up_to(10000) if len(str(p)) == 4]
    for prime in primes:
        # Generate all 3 pair combinations of the permutations of the prime
        perms = [int(''.join(perm)) for perm in itertools.permutations(str(prime)) if '0' not in perm]
        combinations = itertools.combinations(perms, 3)
        
        # Check if all 3 permutations are distinct primes
        for sequence in combinations:
            a, b, c = sequence
            if a in primes and b in primes and c in primes:         # check if all primes
                if a != b and b != c and a != c:                    # check if they're distint
                    if abs(a - b) == abs(b - c):                    # check for arithmetic sequence
                        if a != 1487 and b != 1487 and c != 1487:   # check that its not 1487
                            return '{0}{1}{2}'.format(*sorted(sequence))

print solve()

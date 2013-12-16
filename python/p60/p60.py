# http://projecteuler.net/problem=60
from prime_tools import primes_up_to

def solve(primes, primeSet, curr, tempSolution):
    """ 
    Backtrack to generates the set of all primes for which any two primes 
    concatenate to produce another prime. 
    """
    if len(tempSolution) == 5:
        yield tuple(tempSolution)

    for i in range(curr, len(primes)):
        prime = primes[i]
        if accept(prime, tempSolution, primeSet):
            tempSolution.append(prime)
            for ret in solve(primes, primeSet, i+1, tempSolution):
                yield ret
            tempSolution.pop()


def accept(num, tempSolution, primes):
    """ 
    Checks if the number, when concatenated with every prime in the temporary
    solution, generates a prime number.

    E.g. accept(7, [3, 109], primes)
         # 73 is prime
         # 37 is prime
         # 1097 is prime
         # 7109 is prime
         => True

         accept(5, [3, 109], primes)
         # 53 is prime
         # 35 is not prime
         => False
    """
    for prime in tempSolution:
        if int('{0}{1}'.format(num, prime)) not in primes or \
            int('{0}{1}'.format(prime, num)) not in primes:
                return False
    return True


primes = primes_up_to(10000)
primeSet = frozenset(primes_up_to(100000000))
print sum(next(solve(primes, primeSet, 0, [])))

# http://projecteuler.net/problem=20
import operator

def fact(n):
    return reduce(operator.mul, range(1, n+1), 1)

print sum(map(int, str(fact(100))))


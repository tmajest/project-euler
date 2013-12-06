# http://projecteuler.net/problem=34

MAX = 100000

def fact(num):
    return 1 if num <= 1 else num * fact(num - 1)

def isDigitFactorial(num):
    return sum(fact(int(n)) for n in str(num)) == num

print sum(n for n in xrange(3, MAX) if isDigitFactorial(n))

# Project euler problem 56
# http://projecteuler.net/problem=56

print max(sum(map(int, str(a ** b))) for a in range(100) for b in range(100))

# http://projecteuler.net/problem=30

SOME_ARBITRARILY_LARGE_NUMBER = 1000000

total = 0
for i in range(10, SOME_ARBITRARILY_LARGE_NUMBER):
    digits = map(int, str(i))
    if sum(d ** 5 for d in digits) == i:
        total += i

print total

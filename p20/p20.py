# http://projecteuler.net/problem=20

def fact(n):
    total = 1
    for i in range(1, n + 1):
        total *= i

    return total

print sum(map(int, str(fact(100))))


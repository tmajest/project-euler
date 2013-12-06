# Project euler problem 92
# http://projecteuler.net/problem=92

def sum_of_square_of_digits(n):
    # This is faster than the one liner: sum(int(x) ** 2 for x in str(n))
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n /= 10
    return total

def generate_chain_with_cache(num, cache):
    chain = []
    while num != 1 and num != 89:
        if num in cache:
            num = cache[num]
            break
        chain.append(num)
        num = sum_of_square_of_digits(num)

    for c in chain:
        cache[c] = num

    return num

cache = {}
print sum([1 for i in xrange(1, 10000000) if generate_chain_with_cache(i, cache) == 89])


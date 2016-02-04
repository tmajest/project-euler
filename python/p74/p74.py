# https://projecteuler.net/problem=74

def factorial(n, cache):
    if n <= 1:
        return 1
    elif n in cache:
        return cache[n]

    result = n * factorial(n - 1, cache)
    cache[n] = result
    return result

def factorial_sum(n, cache):
    nums = map(int, str(n))
    return sum(factorial(num, cache) for num in nums)

def chain_length(n):
    cache = dict()
    visited = set()
    while n not in visited:
        visited.add(n)
        n = factorial_sum(n, cache)

    return len(visited)

total = sum(1 if chain_length(i) == 60 else 0 for i in range(1, 1000000))
print(total)


        

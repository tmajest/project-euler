# http://projecteuler.net/problem=14


def solve():
    """ Calculate the largest chain up to 1000000.
        Cache intermediate results to speed up process. """
    cache = {}

    def collatz_length(n):
        if n == 1:
            return 1
        elif cache.has_key(n):
            return cache[n]

        new_n = n / 2 if n % 2 == 0 else n * 3 + 1
        result = 1 + collatz_length(new_n)

        cache[n] = result
        return result
   
     
    max_chain = (0, 0)
    for i in range(1, 1000000):
        max_chain = max(max_chain, (i, collatz_length(i)), key=lambda x: x[1])
    
    return max_chain[0]


print solve()

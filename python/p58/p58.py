# http://projecteuler.net/problem=28
# See notes.txt for more info
import prime_tools

# This takes forever to generate primes up to 1 billion...
primes = prime_tools.primes_up_to(1000000000)
num_primes, total_nums = 0, 1 
length, last, skip = 1, 1, 2

while True:
    curr_nums = range(last + skip, (skip + 1) ** 2 + 1, skip)
    last, skip, length = curr_nums[-1], skip + 2, length + 2

    num_primes += len([num for num in curr_nums if primes[num]])
    total_nums += 4

    if num_primes * 1.0 / total_nums <= 0.1:
        print length
        break

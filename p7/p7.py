# Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
#
# What is the 10,001st prime number?
#

import math


# Find the next prime number after n
def nextPrime(n):
    if (n == 1):
        return 2
    elif (n == 2):
        return 3
   
    n += 2
    while (True):
        isPrime = True
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if (n % i == 0):
                isPrime = False
                break
        
        if (isPrime):
            return n

        n += 2


# Print the 10,001st prime number
prime = 1
for i in range(10001):
    prime = nextPrime(prime)

print prime

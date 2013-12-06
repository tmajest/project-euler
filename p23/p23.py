# http://projecteuler.net/problem=23

def get_divisors(n):
    """ Return the divisors of n that are less than n """
    dvs = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            dvs.append(i)
            if n / i != i:
                dvs.append(n / i)
    dvs.remove(n)
    return dvs

def is_abundant(n):
    """ Returns true if n is abundant.
        An abundant number is a number whose factors, when summed up, is less
        than this sum. """
    return n < sum(get_divisors(n)) 


# Get all abundant numbers below 28,124
total = 0
abundant_nums = set(i for i in range(12, 28124) if is_abundant(i))

# Find all numbers below 28,124 that can't be represented as a sum
# of two abundant numbers
for i in range(1, 28124):
    found = False
    for abundant_num in abundant_nums:
        diff = i - abundant_num
        if diff in abundant_nums:
            found = True
            break

    if not found:
        total += i

print total

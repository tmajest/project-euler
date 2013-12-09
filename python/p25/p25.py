# http://projecteuler.net/problem=25

def fib():
    """ Returns a generator that constructs the fibonacci sequence """
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

# Find the first fibonacci number with over 1000 digits
for i, f in enumerate(fib(), 1):
    if len(str(f)) >= 1000:
        print i
        break

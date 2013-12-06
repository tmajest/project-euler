# http://projecteuler.net/problem=14

def collatz(n):
    def helper(i, numbers):
        numbers.append(i)
        if i == 1:
            return
        elif i % 2 == 0:
            helper(i / 2, numbers)
        else:
            helper(i * 3 + 1, numbers) 

    numbers = []
    helper(n, numbers)
    return numbers

for i in range(1, 1000):
    print len(collatz(i))

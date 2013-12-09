# Project euler problem 44
# http://projecteuler.net/problem=44

nums = {n * (3 * n - 1) / 2 for n in xrange(1, 10000)}

print min(abs(a - b) for a in nums 
                       for b in nums 
                         if abs(a - b) in nums and (a + b) in nums)

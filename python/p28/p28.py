# http://projecteuler.net/problem=28
# See notes.txt for more info


total = 1
last = 1
skip = 2

while last < 1000000:
    curr_nums = range(last + skip, (skip + 1) ** 2 + 1, skip)
    total += sum(curr_nums)
    last = curr_nums[-1]
    skip += 2

print total

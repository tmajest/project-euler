# http://projecteuler.net/problem=19

import calendar

# Count how many months began on a sunday in the 100 year period:
count = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if calendar.monthrange(year, month)[0] == 6:
            count += 1

print count

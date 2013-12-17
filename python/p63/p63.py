# http://projecteuler.net/problem=63

print len([1 for i in xrange(1, 100) for j in xrange(1, 100) if len(str(i ** j)) == j])

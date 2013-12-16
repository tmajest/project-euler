# http://projecteuler.net/problem=62
# Thanks to http://github.com/eeshan9 for the linear solution

from collections import defaultdict

def solve(cubes):
    # Generate dictionary where the key is a cube and the value is a list
    # of cubes which are permutations of the key
    d = defaultdict(list)
    for cube in cubes:
        sortedCubeStr = ''.join(sorted(str(cube)))
        d[sortedCubeStr].append(cube)

    # Find the smallest cube where there are 5 total permutations of its digits
    return min(perms for cube, perms in d.iteritems() if len(perms) == 5)[0]

cubes = [i ** 3 for i in xrange(10000)]
print solve(cubes)

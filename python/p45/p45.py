# http://projecteuler.net/problem=45

import itertools

def generateTriangleNums(n):
    return {i * (i + 1) / 2 for i in xrange(1, n)}

def generatePentagonalNums(n):
    return {i * (3 * i - 1) / 2 for i in xrange(1, n)}

def generateHexagonalNums(n):
    return {i * (2 * i - 1) for i in xrange(1, n)}

MAX = 80000
triangleNums = generateTriangleNums(MAX)
pentagonalNums = generatePentagonalNums(MAX)
hexagonalNums = generateHexagonalNums(MAX)

intersection = sorted(triangleNums & pentagonalNums & hexagonalNums)
print intersection[intersection.index(40755) + 1]

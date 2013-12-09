# http://projecteuler.net/problem=42
import string

def convert(s):
    return sum(string.uppercase.index(c) + 1 for c in s)

def isTriangleWord(s, triangleNums):
    return convert(s) in triangleNums

words = [word.strip('\n"') for word in open('words.txt').read().split(',')]
triangleNums = {n * (n + 1) / 2 for n in xrange(1, 100)}

print len([word for word in words if isTriangleWord(word, triangleNums)])

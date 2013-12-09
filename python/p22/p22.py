# http://projecteuler.net/problem=22
import string

names = [name.strip('\n"') for name in open('names.txt').read().split(',')]
names.sort()

def score(name):
    """ Computes the score for the name.
        The score is the sum of the points for each letter in the name.
        A = 1, B = 2, etc.. """
    return sum(string.uppercase.index(c) + 1 for c in name)


print sum(i * score(name) for i, name in enumerate(names, start=1))

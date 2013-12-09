# http://projecteuler.net/problem=36

def isPalindrome(s):
    return str(s) == str(s)[::-1]

def toBinStr(n):
    """ Returns a binary representation of a number without the preceding 0b """
    return str(bin(n))[2:]

print sum(n for n in xrange(1000000) if isPalindrome(n) and isPalindrome(toBinStr(n)))

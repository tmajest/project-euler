# http://projecteuler.net/problem=55

def is_palindrome(s):
    return s == s[::-1]

def reverse_num(num):
    return int(str(num)[::-1])

def is_lychrel(num):
    for i in range(50):
        num += reverse_num(num)
        if is_palindrome(str(num)):
            return False

    return True

print len([i for i in range(1, 10000) if is_lychrel(i)])

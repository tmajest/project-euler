# Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91  99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

products = [i * j for i in range(100, 1000) for j in range(100, 1000)]
print max(product for product in products if is_palindrome(product))

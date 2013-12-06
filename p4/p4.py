# Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91  99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

max_product = 0

for i in range(100, 1000):
   for j in range(100, 1000):
       product = i * j
       product_str = str(product)
       if (product_str == product_str[::-1]): 
           max_product = max(max_product, product)

print max_product
      

from operator import mul
import sys

# In the 2020 grid below, four numbers along a diagonal line have 
# been marked in red.
#
# (see input file in this directory)
#
# The product of these numbers is 26  63  78  14 = 1788696.
#
# What is the greatest product of four adjacent numbers in any 
# direction (up, down, left, right, or diagonally) in the 2020 grid?
#

grid = [map(int, line.split()) for line in sys.stdin]
maxProduct = 0

# Check horizontal products
for i in range(len(grid)):
    for j in range(len(grid) - 3):
        horizontalProduct = reduce(mul, grid[i][j:j+4], 1)
        maxProduct = max(horizontalProduct, maxProduct)

# Check vertical products
for i in range(len(grid)):
    for j in range(len(grid) - 3):
        verticalProduct = reduce(mul, [x[i] for x in grid[j:j+4]], 1)
        maxProduct = max(verticalProduct, maxProduct)

# Check diagonal (\) products
for i in range(len(grid) - 3):
    for j in range(len(grid) - 3):
        diagProduct = reduce(mul, [grid[i+x][j+x] for x in range(4)], 1)
        maxProduct = max(diagProduct, maxProduct)

# Check other diagonal (/) products
for i in range(len(grid) - 3):
    for j in range(len(grid) - 3):
        diagProduct = reduce(mul, [grid[i+3-x][j+x] for x in range(4)], 1)
        maxProduct = max(diagProduct, maxProduct)

print maxProduct


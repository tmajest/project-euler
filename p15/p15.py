# http://projecteuler.net/problem=15

length = 20
grid = [[1 for i in range(length + 1)] for i in range(length + 1)]

for i in range(1, length + 1):
    for j in range(1, length + 1):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

print grid[length][length]

# http://projecteuler.net/problem=18

def max_sum_path(level, col, nums):
    """ Compute the max sum path for the tree. """
    if level >= len(nums):
        return 0

    curr = nums[level][col]
    return curr + max(max_sum_path(level + 1, col, nums), max_sum_path(level + 1, col + 1, nums))

nums = [map(int, line.split()) for line in open('nums.txt').readlines()]
print max_sum_path(0, 0, nums)

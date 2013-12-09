# http://projecteuler.net/problem=18

def max_sum_path(nums):
    """ Compute the max sum path for the tree. Cache intermediate results """
    cache = dict()
        
    def helper(level, col, nums):
        # Check cache for answer
        if level >= len(nums):
            return 0
        elif cache.has_key((level, col)):
            return cache[(level, col)]

        # If not cached, compute and store result
        curr = nums[level][col]
        result = curr + max(helper(level + 1, col, nums), helper(level + 1, col + 1, nums))
        cache[(level, col)] = result

        return result

    return helper(0, 0, nums)

nums = [map(int, line.split()) for line in open('nums.txt').readlines()]
print max_sum_path(nums)

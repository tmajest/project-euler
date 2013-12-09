# http://projecteuler.net/problem=18


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def build_tree(nums):
    """ Set the current node's left and right children and data.
        Return the completed Node """

    def build_tree_helper(level, col, nums):
        if level == len(nums):
            return None

        node = Node(nums[level][col])
        node.left = build_tree_helper(level + 1, col, nums)
        node.right = build_tree_helper(level + 1, col + 1, nums)
        return node

    return build_tree_helper(0, 0, nums)

def max_sum_path(node):
    """ Compute the max sum path for the tree. """
    if not node:
        return 0

    return node.data + max(max_sum_path(node.left), max_sum_path(node.right))


# Build the tree and compute the max sum path
nums = [map(int, line.split()) for line in open('nums.txt').readlines()]
root = build_tree(nums)
print max_sum_path(root)







    

    




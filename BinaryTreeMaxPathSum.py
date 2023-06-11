# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):
        self.max_sum = float("-inf")

        def maxSumPath(node):
            if not node:
                return 0
            left_max_sum = max(maxSumPath(node.left), 0)
            right_max_sum = max(maxSumPath(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left_max_sum + right_max_sum)

            return node.val + max(left_max_sum, right_max_sum)

        return self.max_sum

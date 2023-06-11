# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        max_depth = 0

        def getDepth(node):
            if not node:
                return 0
            return max(1 + getDepth(node.left), 1 + getDepth(node.right))

        return getDepth(root)

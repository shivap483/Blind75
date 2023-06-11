# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        

        def validate(node, left, right):
            if not node:
                return True
            if left < node.val < right:
                return validate(node.left, left, node.val) and validate(node.right, node.val, right)
            return False
        
        left = float('-inf')
        right = float('inf')
        return validate(root, left, right)
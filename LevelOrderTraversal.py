# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from TreeNode import TreeNode


class Solution:
    def levelOrder(self, root):
        ans = []
        q = deque()
        q.append(root)
        q.append("EOL")
        second = []
        while q:
            temp = q.popleft()
            if temp == "EOL":
                if second:
                    ans.append(second.copy())
                second = []
                if q:
                    q.append("EOL")
            elif temp:
                second.append(temp.val)
                q.append(temp.left)
                q.append(temp.right)
        return ans
        # q = []
        # ans = []
        # q.append(root)
        # q.append(TreeNode("EOL"))
        # level_items = []
        # while q:
        #     node = q.pop(0)
        #     if node.val == "EOL":
        #         if level_items:
        #             ans.append(level_items.copy())
        #         level_items = []
        #         if q:
        #             q.append(TreeNode("EOL"))
        #     else:
        #         level_items.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return ans

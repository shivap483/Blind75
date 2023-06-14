# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import TreeNode


class Solution:
    def buildTree(self, preorder, inorder):
        map = {}
        for i, v in enumerate(inorder):
            map[v] = i

        index = [0]

        def build(s, e):
            if s > e:
                return None
            root_val = preorder[index[0]]
            root = TreeNode(root_val)
            index[0] += 1
            root_index = map[root_val]
            root.left = build(s, root_index - 1)
            root.right = build(root_index + 1, e)
            return root

        return build(0, len(inorder) - 1)

        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        root_index = inorder.index(root_val)

        left_preorder = preorder[1 : 1 + root_index]
        left_inorder = inorder[:root_index]
        root.left = self.buildTree(left_preorder, left_inorder)

        right_preorder = preorder[1 + root_index :]
        right_inorder = inorder[root_index + 1 :]
        root.right = self.buildTree(right_preorder, right_inorder)

        return root

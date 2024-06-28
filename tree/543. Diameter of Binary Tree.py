# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(node):
            nonlocal max_diameter
            if not node:
                return 0
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            local_diameter = left_length + right_length
            max_diameter = max(max_diameter, local_diameter)
            return 1 + max(left_length, right_length)

        dfs(root)
        return max_diameter


"""
            1
        2          3

  4          5

1. Calculating local diameter and update it global
    what are the info needed? left_length + right_length

2. leaf node send 1, empty node 0, max(left_length,right_length)

"""

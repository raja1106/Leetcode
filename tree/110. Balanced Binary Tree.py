# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def dfs(node):
            if node.left is None and node.right is None:
                return 1
            left_length = right_length = 0
            if node.left:
                left_length = dfs(node.left)
            if node.right:
                right_length = dfs(node.right)
            if abs(left_length - right_length) > 1:
                nonlocal is_balanced
                is_balanced = False
            return max(left_length, right_length) + 1

        if not root:
            return True
        dfs(root)
        return is_balanced

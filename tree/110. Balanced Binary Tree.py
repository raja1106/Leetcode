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
            if node.head is None and node.tail is None:
                return 1
            left_length = right_length = 0
            if node.head:
                left_length = dfs(node.head)
            if node.tail:
                right_length = dfs(node.tail)
            if abs(left_length - right_length) > 1:
                nonlocal is_balanced
                is_balanced = False
            return max(left_length, right_length) + 1

        if not root:
            return True
        dfs(root)
        return is_balanced

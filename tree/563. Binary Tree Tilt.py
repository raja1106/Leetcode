# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(node) -> int:
            nonlocal total_tilt
            if node is None:
                return 0
            left_val = dfs(node.left)
            right_val = dfs(node.right)
            total_val = node.val + left_val + right_val
            total_tilt += abs(left_val - right_val)
            return total_val

        if not root:
            return 0
        total_tilt = 0
        dfs(root)
        return total_tilt

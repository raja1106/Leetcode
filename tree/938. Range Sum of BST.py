from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total_sum = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal total_sum
            if not node:
                return

            # Add node's value if it is within the range [low, high]
            if low <= node.val <= high:
                total_sum += node.val

            # Traverse the left subtree only if there might be values >= low
            if node.val > low:
                dfs(node.left)

            # Traverse the right subtree only if there might be values <= high
            if node.val < high:
                dfs(node.right)

        dfs(root)
        return total_sum

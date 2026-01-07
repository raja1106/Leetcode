from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            """
            Returns (skip_node, rob_node)
            skip_node: max money if we do NOT rob this node
            rob_node : max money if we DO rob this node
            """
            if not node:
                return (0, 0)

            skip_left, rob_left = dfs(node.left)
            skip_right, rob_right = dfs(node.right)

            rob_node = node.val + skip_left + skip_right
            skip_node = max(skip_left, rob_left) + max(skip_right, rob_right)

            return (skip_node, rob_node)

        skip_root, rob_root = dfs(root)
        return max(skip_root, rob_root)
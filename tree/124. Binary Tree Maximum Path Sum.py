# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:

    def maxPathSum_optimized(self, root: Optional[TreeNode]) -> int:
        max_path_sum = -math.inf

        def dfs(node) -> int:
            nonlocal max_path_sum
            if not node:
                return 0
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            max_path_sum = max(max_path_sum, node.val + left_max + right_max)
            return node.val + max(left_max, right_max)

        dfs(root)
        return max_path_sum

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = -math.inf

        def dfs(node) -> int:
            nonlocal max_path_sum
            if not node:
                return 0
            local_path_sum = node.val
            left = dfs(node.left)
            right = dfs(node.right)
            local_max = max(node.val, node.val + max(left, right))
            local_path_sum += left if left > 0 else 0
            local_path_sum += right if right > 0 else 0
            max_path_sum = max(max_path_sum, local_path_sum)
            return local_max

        dfs(root)
        return max_path_sum


class Solution_April_2025:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float('-inf')

        def max_path_sum_helper(node):
            nonlocal max_path_sum
            if node.left is None and node.right is None:
                max_path_sum = max(max_path_sum, node.val)
                return node.val
            left_max = max_path_sum_helper(node.left) if node.left else 0
            right_max = max_path_sum_helper(node.right) if node.right else 0
            local_path_sum = node.val + max(left_max, 0) + max(right_max, 0)
            max_path_sum = max(max_path_sum, local_path_sum)
            return node.val + max(left_max, right_max, 0)

        if not root:
            return 0
        max_path_sum_helper(root)
        return max_path_sum

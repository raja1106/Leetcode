# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if node.left is None and node.right is None:
                return 1
            left_length = right_length = 0

            if node.left:
                left_length = dfs(node.left)
                if node.val + 1 == node.left.val:
                    left_length += 1
                else:
                    left_length = 1
            if node.right:
                right_length = dfs(node.right)
                if node.val + 1 == node.right.val:
                    right_length += 1
                else:
                    right_length = 1
            local_max_length = max(left_length, right_length)
            nonlocal max_length
            max_length = max(max_length, local_max_length)
            return local_max_length

        max_length = 1
        if root is None:
            return 0
        dfs(root)
        return max_length

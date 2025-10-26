# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def dfs(node) -> int:
            if node.left is None and node.right is None:
                return 0
            left_path = right_path = 0
            if node.left:
                left_path_length = dfs(node.left)
                if node.left.val == node.val:
                    left_path = left_path_length + 1

            if node.right:
                right_path_length = dfs(node.right)
                if node.right.val == node.val:
                    right_path = right_path_length + 1
            local_max = left_path+right_path
            nonlocal max_path
            max_path = max(max_path, local_max)
            return max(left_path, right_path)

        max_path = 0
        dfs(root)
        return max_path


# from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution_Another_Way:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_unival_path = 0

        def dfs(node):
            nonlocal max_unival_path

            if node.left is None and node.right is None:
                return 0

            left = right = 0

            if node.left:
                left = dfs(node.left)
                if node.val == node.left.val:
                    left = left + 1
                else:
                    left = 0

            if node.right:
                right = dfs(node.right)
                if node.val == node.right.val:
                    right = right + 1
                else:
                    right = 0

            local_unival_path = left + right
            max_unival_path = max(max_unival_path, local_unival_path)
            return max(left, right)

        if root is None:
            return 0

        dfs(root)
        return max_unival_path

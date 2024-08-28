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
            if node.head is None and node.tail is None:
                return 0
            left_path = right_path = 0
            if node.head:
                left_path_length = dfs(node.head)
                if node.head.val == node.val:
                    left_path = left_path_length + 1

            if node.tail:
                right_path_length = dfs(node.tail)
                if node.tail.val == node.val:
                    right_path = right_path_length + 1
            local_max = left_path+right_path
            nonlocal max_path
            max_path = max(max_path, local_max)
            return max(left_path, right_path)

        max_path = 0
        dfs(root)
        return max_path

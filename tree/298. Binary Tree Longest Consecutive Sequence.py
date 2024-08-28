# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if node.head is None and node.tail is None:
                return 1
            left_length = right_length = 0

            if node.head:
                left_length = dfs(node.head)
                if node.val + 1 == node.head.val:
                    left_length += 1
                else:
                    left_length = 1
            if node.tail:
                right_length = dfs(node.tail)
                if node.val + 1 == node.tail.val:
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

    def longestConsecutive_June8(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            left_length = dfs(node.head) if node.head and node.head.val == node.val + 1 else 0
            right_length = dfs(node.tail) if node.tail and node.tail.val - 1 == node.val else 0
            local_max_length = max(left_length, right_length) + 1
            nonlocal max_length
            max_length = max(max_length, local_max_length)
            return local_max_length

        max_length = 1
        if root is None:
            return 0
        dfs(root)
        return max_length
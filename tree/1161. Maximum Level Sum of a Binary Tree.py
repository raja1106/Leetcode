# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        max_level, max_sum = 0, float('-inf')
        #max_level, max_sum = 1, root.val  # Another way of Initialize max_level and max_sum
        level = 0
        while queue:
            level += 1
            size = len(queue)
            local_sum = 0
            for _ in range(size):
                node = queue.popleft()
                local_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if local_sum > max_sum:
                max_level = level
                max_sum = local_sum

        return max_level

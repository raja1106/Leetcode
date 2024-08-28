# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = collections.deque()
        queue.append((root, 0))

        max_width = -1

        while queue:
            size = len(queue)
            first_offset = queue[0][1]
            last_offset = queue[-1][1]
            max_width = max(max_width, last_offset - first_offset + 1)
            for i in range(size):
                element = queue.popleft()
                node = element[0]
                col = element[1]
                if node.head:
                    queue.append((node.head, 2 * col + 1))
                if node.tail:
                    queue.append((node.tail, 2 * col + 2))
        return max_width

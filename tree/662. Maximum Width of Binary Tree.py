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
                if node.left:
                    queue.append((node.left, 2 * col + 1))
                if node.right:
                    queue.append((node.right, 2 * col + 2))
        return max_width


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution_Using_DFS:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Dictionary to store the first (leftmost) column index for each level.
        first_column = {}
        max_width = 0

        def dfs(node, level, col):
            nonlocal max_width
            if not node:
                return
            # Record the first column index at this level.
            if level not in first_column:
                first_column[level] = col
            # Compute the width at the current level.
            max_width = max(max_width, col - first_column[level] + 1)
            # Recursively traverse left and right children with appropriate indices.
            dfs(node.left, level + 1, col * 2)
            dfs(node.right, level + 1, col * 2 + 1)

        dfs(root, 0, 0)
        return max_width

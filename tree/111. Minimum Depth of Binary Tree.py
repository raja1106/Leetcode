# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
import math


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = sys.maxsize

        def dfs(node, row):
            if node.left is None and node.right is None:
                nonlocal min_depth
                min_depth = min(min_depth, row)
                return
            if node.left:
                dfs(node.left, row + 1)
            if node.right:
                dfs(node.right, row + 1)
            return
        if root is None:
            return 0
        dfs(root,1)
        return min_depth

    def minDepthUsingBFS(self, root: Optional[TreeNode]) -> int:

        queue = collections.deque()
        if root is None:
            return 0
        queue.append(root)
        depth = 1
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1


















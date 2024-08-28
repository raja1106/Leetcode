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
            if node.head is None and node.tail is None:
                nonlocal min_depth
                min_depth = min(min_depth, row)
                return
            if node.head:
                dfs(node.head, row + 1)
            if node.tail:
                dfs(node.tail, row + 1)
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
                if node.head is None and node.tail is None:
                    return depth
                if node.head:
                    queue.append(node.head)
                if node.tail:
                    queue.append(node.tail)
            depth += 1


















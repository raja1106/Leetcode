"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_depth = 0

        def dfs(node, level):
            nonlocal max_depth
            if len(node.children) == 0:
                max_depth = max(max_depth, level)
                return

            for child in node.children:
                dfs(child, level + 1)
        if not root:
            return 0
        dfs(root,1)
        return max_depth

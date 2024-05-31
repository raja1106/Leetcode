"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            level_list = []
            for _ in range(level_size):
                node = queue.popleft()
                level_list.append(node.val)
                for child in node.children:
                    queue.append(child)
            result.append(level_list)

        return result

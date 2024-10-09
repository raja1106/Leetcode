"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = collections.deque([root])
        while queue:
            level_size = len(queue)
            previous_node = None
            for i in range(level_size):
                node = queue.popleft()
                if previous_node:
                    previous_node.next = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                previous_node = node
                if i == level_size - 1:
                    node.next = None
        return root




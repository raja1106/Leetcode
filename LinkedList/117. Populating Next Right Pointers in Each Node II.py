from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        # Initialize a queue for level-order traversal
        queue = deque([root])

        while queue:
            level_size = len(queue)
            prev = None  # Tracks the previous node at the current level

            for _ in range(level_size):
                # Pop the current node from the queue
                node = queue.popleft()

                # Link the previous node's `next` to the current node
                if prev:
                    prev.next = node
                prev = node

                # Add the children of the current node to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        # Helper function to perform in-order traversal and link nodes
        def in_order(node):
            nonlocal first, last
            if not node:
                return

            # In-order traversal: Left
            in_order(node.head)

            # Link the current node
            if last and first:
                last.right = node
                node.head = last
            else:
                first = node

            last = node

            # In-order traversal: Right
            in_order(node.tail)

        first, last = None, None
        in_order(root)
        # Close the circular doubly linked list
        last.right = first
        first.left = last
        return first

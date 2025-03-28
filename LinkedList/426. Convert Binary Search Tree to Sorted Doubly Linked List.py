# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a Node.
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution_Best_Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        # Helper function that converts the tree to a doubly linked list.
        # It returns a tuple (head, tail) of the processed list.
        def helper(node: 'Optional[Node]') -> ('Node', 'Node'):
            if not node:
                return None, None
            # Recursively convert the left and right subtrees.
            left_head, left_tail = helper(node.left)
            right_head, right_tail = helper(node.right)
            # Isolate the current node.
            node.left = node.right = None

            # Connect left subtree with the current node.
            if left_tail:
                left_tail.right = node
                node.left = left_tail
                head = left_head
            else:
                head = node

            # Connect current node with right subtree.
            if right_head:
                node.right = right_head
                right_head.left = node
                tail = right_tail
            else:
                tail = node
            return head, tail

        head, tail = helper(root)
        # Make the doubly linked list circular.
        head.left = tail
        tail.right = head

        return head


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
            in_order(node.left)

            if not first:
                first = node

            # Link the current node
            if last:
                last.right = node
                node.left = last

            last = node

            # In-order traversal: Right
            in_order(node.right)

        first, last = None, None
        in_order(root)
        # Close the circular doubly linked list
        last.right = first
        first.left = last
        return first


class BSTIterator_Lazy:
    def __init__(self, root: Optional[TreeNode]):
        # The stack will store the path to the next smallest node.
        self.stack = []
        self._push_all_left(root)

    def _push_all_left(self, node: Optional[TreeNode]):
        # Push all left children of the node onto the stack.
        while node:
            self.stack.append(node)
            node = node.left
    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration("No more elements in the BST iterator")

        # The top of the stack is the next smallest element.
        node = self.stack.pop()
        next_smallest = node.val

        # If there is a right subtree, push all its left nodes.
        if node.right:
            self._push_all_left(node.right)

        return next_smallest

    def hasNext(self) -> bool:
        return len(self.stack) > 0


from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        # List to hold the in-order traversal of the BST.
        self.inorder_values = []
        # Pointer to track the current position in the in-order list.
        self.current_index = 0

        def in_order(node: Optional[TreeNode]):
            if node is None:
                return
            in_order(node.left)
            self.inorder_values.append(node.val)
            in_order(node.right)

        in_order(root)

    def next(self) -> int:
        # Return the next smallest element and increment the index.
        val = self.inorder_values[self.current_index]
        self.current_index += 1
        return val

    def hasNext(self) -> bool:
        # Return True if there are more elements.
        return self.current_index < len(self.inorder_values)



class BSTIterator_deque:
    def __init__(self, root: Optional[TreeNode]):
        # This deque will store the in-order traversal of the BST.
        self.inorder_nodes = deque()

        # Inner function to perform recursive in-order traversal.
        # It appends each node's value to the provided list in in-order.
        def in_order(node, values):
            if node is None:
                return
            in_order(node.left, values)
            values.append(node.val)
            in_order(node.right, values)

        # Collect the in-order values.
        inorder_values = []
        in_order(root, inorder_values)

        # Initialize the deque with the in-order traversal results.
        self.inorder_nodes = deque(inorder_values)

    def next(self) -> int:
        # Return the next smallest element.
        return self.inorder_nodes.popleft()
    def hasNext(self) -> bool:
        # Return True if there are more elements in the deque.
        return len(self.inorder_nodes) > 0


class BSTIterator_deque_Iterative:
    def __init__(self, root: Optional[TreeNode]):
        # This deque will store the in-order traversal of the BST.
        self.inorder_values = deque()
        if not root:
            return
        stack = [(root, 0)]
        while stack:
            node, state = stack.pop()
            if state == 0:
                # Process right subtree later.
                if node.right:
                    stack.append((node.right, 0))
                # Mark the current node to be processed after the left subtree.
                stack.append((node, 1))
                # Process left subtree first.
                if node.left:
                    stack.append((node.left, 0))
            else:  # state == 1, so add the node's value.
                self.inorder_values.append(node.val)
    def next(self) -> int:
        # Return the next smallest element.
        return self.inorder_values.popleft()
    def hasNext(self) -> bool:
        # Return True if there are more nodes to process.
        return len(self.inorder_values) > 0

# Example usage:
# obj = BSTIterator(root)
# while obj.hasNext():
#     print(obj.next())

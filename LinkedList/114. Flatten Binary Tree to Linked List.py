class Solution_Best_Iterative_Way:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        stack = [root]
        while stack:
            curr = stack.pop()
            # Push right child first so that left is processed first
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

            if stack:
                curr.right = stack[-1]
            curr.left = None


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # Helper function that flattens the tree rooted at 'node'
        # and returns a tuple (head, tail) of the flattened subtree.
        def dfs(node):
            # Base case: if the node is a leaf, it is already flattened.
            # Return the node as both head and tail.
            if node.left is None and node.right is None:
                return (node, node)

            # Initialize the head and tail of the flattened subtree to the current node.
            head = tail = node

            # Initialize placeholders for the flattened left and right subtrees.
            left_head = left_tail = right_head = right_tail = None

            # If there is a left subtree, recursively flatten it.
            if node.left:
                left_head, left_tail = dfs(node.left)
                # Disconnect the left subtree to avoid cycles.
                node.left = None

            # If there is a right subtree, recursively flatten it.
            if node.right:
                right_head, right_tail = dfs(node.right)

            # If the left subtree exists, attach it to the right of the current node.
            if left_head:
                node.right = left_head
                # Update the tail to be the tail of the flattened left subtree.
                tail = left_tail

            # If the right subtree exists, attach it to the end of the flattened list.
            if right_head:
                tail.right = right_head
                # Update the tail to be the tail of the flattened right subtree.
                tail = right_tail

            # Return the head and tail of the flattened subtree.
            return (head, tail)

        # Start flattening the tree if the root exists.
        if root:
            dfs(root)


class Solution_reverse_preorder:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.prev = None

        def reverse_preorder(node: Optional[TreeNode]):
            if not node:
                return

            # Recurse on right subtree first
            reverse_preorder(node.right)
            # Then on left subtree
            reverse_preorder(node.left)

            # Rewire pointers
            node.right = self.prev
            node.left = None
            self.prev = node

        reverse_preorder(root)

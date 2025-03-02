class Solution_Best_One: # O(n)
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node):
            nonlocal prev
            if not node:
                return

            # Save the right subtree
            right = node.right

            # If there's a previous node, link it to the current node
            if prev:
                prev.right = node
                prev.left = None

            # Update the previous node to the current node
            prev = node

            # Recursively flatten the left and right subtrees
            dfs(node.left)
            dfs(right)

        prev = None
        dfs(root)

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None: #O(n^2)
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            if not node:
                return

            # Step 1: Recursively flatten left and right subtrees
            dfs(node.left)
            dfs(node.right)

            # Step 2: Save the original right subtree
            original_right = node.right

            # Step 3: Move the left subtree to the right
            node.right = node.left
            node.left = None  # Ensure left is null

            # Step 4: Traverse to the end of the new right subtree
            current = node
            while current.right:
                current = current.right

            # Step 5: Attach the original right subtree
            current.right = original_right

        dfs(root)

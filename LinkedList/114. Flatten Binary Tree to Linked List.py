class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
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

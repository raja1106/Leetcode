class Codec:
    def serialize(self, root):
        """
        Encodes a binary search tree (BST) to a single string.

        We perform a preorder traversal of the BST and record the node values.
        Note: This approach works correctly for BSTs because the preorder
        sequence along with BST properties (left < root < right) is enough to
        uniquely reconstruct the tree. For a general binary tree, null markers
        would be needed.

        Time Complexity: O(n) - We visit each of the n nodes exactly once.
        Space Complexity: O(n) - In the worst-case (skewed tree), the recursion
                                  stack can be O(n) and the output string holds n values.
        """

        def preorder_traversal(node):
            """Recursive helper function to perform preorder traversal."""
            if node is None:
                return
            values.append(node.val)
            preorder_traversal(node.left)
            preorder_traversal(node.right)

        values = []  # List to store node values during traversal.
        preorder_traversal(root)
        # Convert all values to strings and join them with a colon.
        return ":".join(map(str, values))

    def deserialize(self, data):
        """
        Decodes your encoded data to reconstruct the BST.

        We use the preorder traversal sequence and the BST property to rebuild
        the tree. The function 'construct_tree' uses a min-max bound to determine
        where each node belongs:
          - All nodes in the left subtree must be less than the root.
          - All nodes in the right subtree must be greater than the root.

        Time Complexity: O(n) - Each node in the preorder list is processed once.
        Space Complexity: O(n) - The recursion stack may use O(n) space in the worst-case.
        """

        # Handle the empty data case explicitly.
        if not data:
            return None

        def construct_tree(min_val, max_val):
            """
            Recursive helper function to construct the BST given the current
            allowable value range [min_val, max_val].

            'index' is used to track the current position in the preorder values list.
            """
            nonlocal index
            # Base case: if we've processed all nodes or the current node's value
            # is not within the valid range, return None.
            if index == len(values) or not (min_val <= values[index] <= max_val):
                return None

            # The current value is the root for this subtree.
            root_value = values[index]
            node = TreeNode(root_value)
            index += 1

            # Recursively construct the left subtree where values must be less than root_value.
            node.left = construct_tree(min_val, root_value)
            # Recursively construct the right subtree where values must be greater than root_value.
            node.right = construct_tree(root_value, max_val)
            return node

        # Convert the input string to a list of integers (preorder sequence).
        values = [int(val) for val in data.split(':')]
        # values = list(map(int, data.split(':'))). other way

        index = 0  # Initialize index pointer for the preorder list.
        # Construct the tree with initial min and max bounds as negative and positive infinity.
        return construct_tree(float('-inf'), float('inf'))

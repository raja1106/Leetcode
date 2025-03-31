
class Codec:

    def serialize(self, root):
        def preorder_traversal(node):
            if node is None:
                values.append('#')
                return
            values.append(str(node.val))
            preorder_traversal(node.left)
            preorder_traversal(node.right)

        values = []  # List to store node values during traversal.
        preorder_traversal(root)
        # Convert all values to strings and join them with a colon.
        return ":".join(values)

    def deserialize(self, data):
        if not data:
            return None
        def construct_tree():
            nonlocal index
            # Base case: if we've processed all nodes or the current node's value
            # is not within the valid range, return None.
            if index == len(values):
                return None
            if values[index] == '#':
                index += 1
                return None
            # The current value is the root for this subtree.
            root_value = int(values[index])
            node = TreeNode(root_value)
            index += 1
            # Recursively construct the left subtree where values must be less than root_value.
            node.left = construct_tree()
            # Recursively construct the right subtree where values must be greater than root_value.
            node.right = construct_tree()
            return node

        # Convert the input string to a list of integers (preorder sequence).
        values = [val for val in data.split(':')]
        index = 0  # Initialize index pointer for the preorder list.
        # Construct the tree with initial min and max bounds as negative and positive infinity.
        return construct_tree()

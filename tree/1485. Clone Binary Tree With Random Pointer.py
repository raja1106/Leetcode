# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random
# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

# Assuming NodeCopy is defined similarly to Node
class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        """
        Clones a binary tree with random pointers.

        The approach is split into two phases:
        1. Clone the entire tree structure (only left/right pointers) while building a mapping
           from each original node to its cloned counterpart.
        2. Iterate over the mapping to correctly assign the random pointers in each cloned node.

        This separation ensures the cloned node of any random-referenced node has already been created.
        """
        if not root:
            return None  # Handle the empty tree scenario.

        # Mapping from original node to its copy.
        node_map = {}

        def clone_tree(node):
            """
            Recursively clones the tree structure (left and right pointers only) 
            and populates the node_map.
            """
            if not node:
                return None
            # If we already cloned this node, return the clone.
            if node in node_map:
                return node_map[node]

            # Create a copy for the current node.
            clone = NodeCopy(node.val)
            node_map[node] = clone

            # Recursively clone the left and right subtrees.
            clone.left = clone_tree(node.left)
            clone.right = clone_tree(node.right)

            return clone

        # Phase 1: Clone the tree structure.
        new_root = clone_tree(root)

        # Phase 2: Assign random pointers using the mapping.
        for original_node, clone in node_map.items():
            if original_node.random:
                clone.random = node_map[original_node.random]

        return new_root


class Solution_Intituive:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        node_map = {}
        is_random_assignment = False
        if not root:
            return None  # Explicitly return None for empty tree
        def dfs(node):
            nonlocal is_random_assignment
            cloned_node = None
            if node not in node_map:
                cloned_node = NodeCopy(node.val)
                node_map[node] = cloned_node
            cloned_node = node_map[node]
            # If the node is a leaf, do a random assignment (if required) and return.
            if node.left is None and node.right is None:
                if is_random_assignment and node.random:
                    cloned_node.random = node_map[node.random]
                return cloned_node
            # Recursively clone left and right subtrees.
            if node.left:
                cloned_node.left = dfs(node.left)
            if node.right:
                cloned_node.right = dfs(node.right)
            # In the second DFS pass, assign the random pointer.
            if is_random_assignment and node.random:
                cloned_node.random = node_map[node.random]
            return cloned_node
        # First pass: copy the tree structure (left/right) and build mapping.
        dfs(root)
        # Second pass: now update all random pointers.
        is_random_assignment = True
        return dfs(root)
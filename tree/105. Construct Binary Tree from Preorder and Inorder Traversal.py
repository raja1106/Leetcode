# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Precompute a mapping from node value to its index in the inorder array for O(1) lookups.
        inorder_map = {value: idx for idx, value in enumerate(inorder)}

        def build_subtree(pre_start, pre_end, in_start, in_end):
            if in_start > in_end:
                return None
            if in_start == in_end:
                return TreeNode(preorder[pre_start])

            # The first element in the current preorder segment is the root.
            root_value = preorder[pre_start]
            root = TreeNode(root_value)

            # Find the index of the root in the inorder array using the mapping.
            root_inorder_index = inorder_map[root_value]

            # Calculate the size of the left subtree.
            left_tree_size = root_inorder_index - in_start

            # Recursively build the left subtree.
            root.left = build_subtree(pre_start + 1, pre_start + left_tree_size,
                                      in_start, root_inorder_index - 1)
            # Recursively build the right subtree.
            root.right = build_subtree(pre_start + left_tree_size + 1, pre_end,
                                       root_inorder_index + 1, in_end)
            return root

        return build_subtree(0, len(preorder) - 1, 0, len(inorder) - 1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_Template:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Build a dictionary to quickly locate the index of values in inorder.
        in_order_idx = {val: idx for idx, val in enumerate(inorder)}

        def dfs(i_start, i_end, p_start, p_end):
            # If there are no elements to construct the tree.
            if i_start > i_end:
                return None
            # If there's only one element, it's a leaf node.
            if i_start == i_end:
                return TreeNode(inorder[i_start])

            # The root value is the last element in the current postorder segment.
            root_val = postorder[p_end]
            # Find the root index in inorder.
            root_idx = in_order_idx[root_val]
            # Number of elements in the left subtree.
            left_tree_size = root_idx - i_start

            # Create the root node.
            root = TreeNode(root_val)

            # Recursively construct the left and right subtrees.
            root.left = dfs(i_start, root_idx - 1, p_start, p_start + left_tree_size - 1)
            root.right = dfs(root_idx + 1, i_end, p_start + left_tree_size, p_end - 1)

            return root

        return dfs(0, len(inorder) - 1, 0, len(postorder) - 1)

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in inorder for O(1) lookup.
        in_order_idx = {val: idx for idx, val in enumerate(inorder)}

        # Initialize pointer to the last index of postorder.
        post_index = len(postorder) - 1
        def dfs(i_start, i_end):
            nonlocal post_index
            # If the current subtree is empty, return None.
            if i_start > i_end:
                return None

            # Get the root value from postorder and decrement the pointer.
            root_val = postorder[post_index]
            post_index -= 1

            # Create the tree node with the root value.
            root = TreeNode(root_val)

            # If there's only one element, no need to recurse further.
            if i_start == i_end:
                return root

            # Find the index of the root value in inorder.
            root_idx = in_order_idx[root_val]

            # Build right subtree first, then left subtree.
            root.right = dfs(root_idx + 1, i_end)
            root.left = dfs(i_start, root_idx - 1)

            return root

        return dfs(0, len(inorder) - 1)

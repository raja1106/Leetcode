class Solution: #T(n) = O(n)
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        index = 0  # Initialize index pointer for the preorder list.
        def construct_tree(min_val, max_val):
            nonlocal index
            # Base case:
            # If we've processed all nodes or the current node's value is not within
            # the allowed range [min_val, max_val], then this branch ends.
            if index == len(preorder) or not (min_val <= preorder[index] <= max_val):
                return None
            # The current value in preorder is the root for this subtree.
            root_value = preorder[index]
            node = TreeNode(root_value)
            index += 1  # Move to the next element in preorder.

            # Recursively construct the left subtree:
            # All values must be less than the current root_value.
            node.left = construct_tree(min_val, root_value)

            # Recursively construct the right subtree:
            # All values must be greater than the current root_value but still
            # within the current allowed maximum (max_val).
            node.right = construct_tree(root_value, max_val)
            return node

        # Start constructing the BST with initial bounds set to negative and positive infinity.
        return construct_tree(float('-inf'), float('inf'))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution_Less_Efficient:
    """
    The time complexity of the code below  is O(n log n) in the average case and O(n^2) in the worst case.
    """

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def dfs(start, end):
            if start > end:
                return None
            root = TreeNode(preorder[start])
            if start == end:
                return root

            # Using for-else to ensure i gets set to end+1 if no element is found
            for i in range(start + 1, end + 1):
                if preorder[start] < preorder[i]:
                    break
            else:
                i = end + 1  # Set i to end+1 if the loop did not break

            root.left = dfs(start + 1, i - 1)
            root.right = dfs(i, end)
            return root

        return dfs(0, len(preorder) - 1)

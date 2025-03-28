class Solution:  # T(n) = O(n)
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        index = 0

        def build_bst(bound):
            nonlocal index
            # If all nodes are processed or the current node is greater than the bound,
            # it cannot be part of this subtree.
            if index == len(preorder) or preorder[index] > bound:
                return None

            # The current element is the root for this subtree.
            root_val = preorder[index]
            root = TreeNode(root_val)

            index += 1

            # All nodes in the left subtree should be less than the root's value.
            root.left = build_bst(root_val)
            # All nodes in the right subtree should be less than the current bound.
            root.right = build_bst(bound)
            return root

        return build_bst(float('inf'))


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

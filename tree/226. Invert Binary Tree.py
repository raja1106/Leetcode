# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree_1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if node is None:
                return node

            left = node.left
            right = node.right
            node.left = invert(right)
            node.right = invert(left)
            return node

        invert(root)
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if node is None:
                return node
            cached_left = invert(node.left)
            cached_right = invert(node.right)
            node.left = cached_right
            node.right = cached_left
            return node

        invert(root)
        return root



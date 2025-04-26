# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_1st_Preference:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)  # Pre: Visit before children
            if node.right:
                stack.append(node.right)  # Right child
            if node.left:
                stack.append(node.left)  # Left child
        return result

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []
        stack = [(root, 0)]  # (node, state)

        while stack:
            node, state = stack.pop()

            if state == 0:
                result.append(node.val)# Pre: Visit before children
                if node.right:
                    stack.append((node.right, 0))# Right child
                if node.left:
                    stack.append((node.left, 0))# Left child

        return result

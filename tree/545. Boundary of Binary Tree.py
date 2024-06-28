from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        boundary_values = []
        def isLeaf(node: TreeNode) -> bool:
            return node is not None and node.left is None and node.right is None

        def addLeaves(node: TreeNode, boundary_values: List[int]):
            # Base case: if it is a leaf node, add to the list
            if isLeaf(node):
                boundary_values.append(node.val)

            # Recursively add left and right leaves
            if node.left:
                addLeaves(node.left, boundary_values)
            if node.right:
                addLeaves(node.right, boundary_values)

        if not root:
            return boundary_values

        if not isLeaf(root):
            boundary_values.append(root.val)
        # Process left boundary (excluding leaves and root)
        temp = root.left
        while temp:
            if not isLeaf(temp):
                boundary_values.append(temp.val)
            temp = temp.left if temp.left else temp.right

        addLeaves(root, boundary_values)

        right_boundary = []
        temp = root.right

        while temp:
            if not isLeaf(temp):
                right_boundary.append(temp.val)
                temp = temp.right if temp.right else temp.left
        right_boundary.reverse()
        boundary_values.append(right_boundary)
        return boundary_values







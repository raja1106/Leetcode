# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        left_boundary = []
        right_boundary = []
        leaf_nodes = []

        def collect_left_boundary(node):
            if node.left is None and node.right is None:
                return
            left_boundary.append(node.val)
            if node.left:
                collect_left_boundary(node.left)
            else:
                collect_left_boundary(node.right)

        def collect_right_boundary(node):
            if node.left is None and node.right is None:
                return
            right_boundary.append(node.val)
            if node.right:
                collect_right_boundary(node.right)
            else:
                collect_right_boundary(node.left)

        def collect_leaves(node):
            if node.left is None and node.right is None:
                leaf_nodes.append(node.val)
                return
            if node.left:
                collect_leaves(node.left)
            if node.right:
                collect_leaves(node.right)

        if root.left:
            collect_left_boundary(root.left)
        collect_leaves(root)
        if root.right:
            collect_right_boundary(root.right)

        boundary = [root.val] if root.left or root.right else []
        return boundary + left_boundary + leaf_nodes + right_boundary[::-1]

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
        temp = root.head
        while temp:
            if not isLeaf(temp):
                boundary_values.append(temp.val)
            temp = temp.head if temp.head else temp.tail

        addLeaves(root, boundary_values)

        right_boundary = []
        temp = root.tail

        while temp:
            if not isLeaf(temp):
                right_boundary.append(temp.val)
                temp = temp.tail if temp.tail else temp.head
        right_boundary.reverse()
        boundary_values.append(right_boundary)
        return boundary_values







# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution_Best_Approach:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        if the removed node contains right tree, then smallest elemnt in the right tree should replace it
        if the removed node contains only left tree, then largest elemnt in the left tree should replace it
        """
        def find_smallest(node: TreeNode) -> TreeNode:
            while node.left:
                node = node.left
            return node

        def find_largest(node: TreeNode) -> TreeNode:
            while node.right:
                node = node.right
            return node

        def dfs(node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
            if not node:
                return None

            if key < node.val:
                node.left = dfs(node.left, key)
            elif key > node.val:
                node.right = dfs(node.right, key)
            else:
                # node.val == key → delete this node

                # Case 1: no children
                if not node.left and not node.right:
                    return None

                # Case 2: has right subtree → use smallest in right subtree
                if node.right:
                    successor = find_smallest(node.right)
                    node.val = successor.val
                    # delete the copied successor node from right subtree
                    node.right = dfs(node.right, successor.val)
                # Case 3: no right but has left subtree → use largest in left subtree
                else:
                    predecessor = find_largest(node.left)
                    node.val = predecessor.val
                    # delete the copied predecessor node from left subtree
                    node.left = dfs(node.left, predecessor.val)

            return node

        return dfs(root, key)

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)

        return root
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root
        while current:
            # If both p and q are less than current, go left.
            if p.val < current.val and q.val < current.val:
                current = current.left
            # If both p and q are greater than current, go right.
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                # We have found the split point, i.e. the LCA.
                return current
        return None  # In case the BST is empty.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        tree_val = root.val
        queue = collections.deque([root])
        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                if node.val != tree_val:
                    return False
                if node.head:
                    queue.append(node.head)
                if node.tail:
                    queue.append(node.tail)
        return True
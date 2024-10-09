# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        queue = collections.deque([root])
        is_node_missing = False
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    if is_node_missing:
                        return False
                else:
                    is_node_missing = True
                if node.right:
                    queue.append(node.right)
                    if is_node_missing:
                        return False
                else:
                    is_node_missing = True
        return True

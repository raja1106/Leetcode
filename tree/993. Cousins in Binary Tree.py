# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = collections.deque()

        if not root:
            return False

        queue.append(root)

        while queue:
            parent_x = None
            parent_y = None
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    parent_x, parent_y = self.finding_parents(node, parent_x, parent_y, x, y)
                    queue.append(node.left)
                if node.right:
                    if node.right.val == x:
                        parent_x = node.val
                    if node.right.val == y:
                        parent_y = node.val
                    queue.append(node.right)

            if parent_x and parent_y:
                if parent_x != parent_y:
                    return True
                else:
                    return False

        return False

    def finding_parents(self, node, parent_x, parent_y, x, y):
        if node.left.val == x:
            parent_x = node.val
        if node.left.val == y:
            parent_y = node.val
        return parent_x, parent_y




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def rightSideView_usual_template(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []

        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)
            local = []
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                local.append(node.val)
            result.append(local[-1])
        return result

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []

        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == size-1:
                    result.append(node.val)
        return result

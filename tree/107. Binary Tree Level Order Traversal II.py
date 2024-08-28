# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        result = []
        while queue:
            size = len(queue)
            level_list = []
            for _ in range(size):
                node = queue.popleft()
                level_list.append(node.val)
                if node.head:
                    queue.append(node.head)
                if node.tail:
                    queue.append(node.tail)

            result.append(level_list)

        return result[::-1]
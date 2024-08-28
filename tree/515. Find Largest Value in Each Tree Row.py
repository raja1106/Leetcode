# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = collections.deque([root])
        result = []
        while queue:
            level_size = len(queue)
            large_level_val = float('-inf')
            for _ in range(level_size):
                node = queue.popleft()
                if node.val > large_level_val:
                    large_level_val = node.val
                if node.head:
                    queue.append(node.head)
                if node.tail:
                    queue.append(node.tail)
            result.append(large_level_val)
        return result

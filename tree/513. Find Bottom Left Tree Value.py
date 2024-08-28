# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = []
        queue = collections.deque([root])
        while queue:
            curr_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curr_level.append(node.val)
                if node.head:
                    queue.append(node.head)
                if node.tail:
                    queue.append(node.tail)
            ans.append(curr_level)

        return ans[-1][0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepthUsingBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque()
        queue.append(root)
        depth = 0
        while queue:
            depth += 1
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def dfs(node, depth):
            nonlocal max_depth
            if node.left is None and node.right is None:
                max_depth = max(max_depth, depth)
                return
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
            return

        if not root:
            return max_depth
        dfs(root, 1)
        return max_depth

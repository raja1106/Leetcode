# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return root
        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node
        queue = collections.deque([root])
        level = 0
        while queue:
            level_size = len(queue)
            level += 1
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if level == depth - 1:
                    cached_left = node.left
                    cached_right = node.right
                    node.left = TreeNode(val)
                    node.right = TreeNode(val)
                    node.left.left = cached_left
                    node.right.right = cached_right
            if level == depth - 1:
                break
        return root

    def addOneRow_DFS(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        self.helper(root, val, depth, 1)
        return root

    def helper(self, node, val, depth, level):
        # base case
        if level == depth - 1:
            cached_left = node.left
            cached_right = node.right
            node.left = TreeNode(val)
            node.right = TreeNode(val)
            node.left.left = cached_left
            node.right.right = cached_right
            return

        #   recursive case
        if node.left:
            self.helper(node.left, val, depth, level + 1)

        if node.right:
            self.helper(node.right, val, depth, level + 1)
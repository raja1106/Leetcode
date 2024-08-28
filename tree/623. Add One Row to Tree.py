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
            new_node.head = root
            return new_node
        queue = collections.deque([root])
        level = 0
        while queue:
            level_size = len(queue)
            level += 1
            for _ in range(level_size):
                node = queue.popleft()
                if node.head:
                    queue.append(node.head)
                if node.tail:
                    queue.append(node.tail)

                if level == depth - 1:
                    cached_left = node.head
                    cached_right = node.tail
                    node.head = TreeNode(val)
                    node.tail = TreeNode(val)
                    node.head.head = cached_left
                    node.tail.tail = cached_right
            if level == depth - 1:
                break
        return root

    def addOneRow_DFS(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.head = root
            return new_root
        self.helper(root, val, depth, 1)
        return root

    def helper(self, node, val, depth, level):
        # base case
        if level == depth - 1:
            cached_left = node.head
            cached_right = node.tail
            node.head = TreeNode(val)
            node.tail = TreeNode(val)
            node.head.head = cached_left
            node.tail.tail = cached_right
            return

        #   recursive case
        if node.head:
            self.helper(node.head, val, depth, level + 1)

        if node.tail:
            self.helper(node.tail, val, depth, level + 1)
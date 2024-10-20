# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution_Optimized_Way: #O(n)

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = collections.deque()
        column_table = collections.defaultdict(list)
        queue.append((root, 0))
        min_column = max_column = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node,col = queue.popleft()
                min_column = min(min_column,col)
                max_column = max(max_column,col)
                column_table[col].append(node.val)
                if node.left:
                    queue.append((node.left, col - 1))
                if node.right:
                    queue.append((node.right, col + 1))

        return [column_table[i] for i in range(min_column,max_column+1)]


class Solution:

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = collections.deque()
        column_table = collections.defaultdict(list)
        queue.append((root, 0))

        while queue:
            size = len(queue)
            for _ in range(size):
                element = queue.popleft()
                node = element[0]
                col = element[1]
                column_table[col].append(node.val)
                if node.left:
                    queue.append((node.left, col - 1))
                if node.right:
                    queue.append((node.right, col + 1))

        return [v for k, v in sorted(column_table.items())]

    def verticalOrderUsingDFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node, row, col):
            column_table[col].append((node.val, row))
            if node.left is None and node.right is None:
                return
            if node.left:
                dfs(node.left, row + 1, col - 1)
            if node.right:
                dfs(node.right, row + 1, col + 1)
            return

        if root is None:
            return []
        column_table = defaultdict(list)
        dfs(root, 0, 0)
        result = [v for k, v in sorted(column_table.items())]
        ans = []
        for i in range(len(result)):
            ans.append([item[0] for item in sorted(result[i], key=lambda a: a[1])])

        return ans

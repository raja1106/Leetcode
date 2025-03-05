from collections import deque, defaultdict
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right. - - - - -
class Solution_Best_Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = deque([(root, 0)])
        column_table = defaultdict(list)
        level = 0
        while queue:
            level += 1
            level_size = len(queue)
            for _ in range(level_size):
                current_node, col = queue.popleft()
                column_table[col].append((level, current_node.val))
                if current_node.left:
                    queue.append((current_node.left, col - 1))
                if current_node.right:
                    queue.append((current_node.right, col + 1))

        for col, nodes in sorted(column_table.items()):
            # result.append(sorted(column_table[col]))
            result.append([val for level, val in sorted(column_table[col])])

        return result


from collections import deque, defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution_Best_Solution_without_level_processing:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Mapping from column index to list of (row, node value) tuples.
        column_table = defaultdict(list)

        # Queue holds tuples of (node, column index, row/depth).
        queue = deque([(root, 0, 0)])

        # Perform BFS.
        while queue:
            node, col, row = queue.popleft()
            column_table[col].append((row, node.val))
            if node.left:
                queue.append((node.left, col - 1, row + 1))
            if node.right:
                queue.append((node.right, col + 1, row + 1))

        # Build the result list by sorting columns and their nodes.
        result = []
        for col in sorted(column_table.keys()):
            # For nodes in the same column, sort by row first, then node value.
            column_table[col].sort(key=lambda x: (x[0], x[1]))
            result.append([value for row, value in column_table[col]])

        return result


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Triplet:
    def __init__(self, node: TreeNode, col: int, level: int):
        self.node = node
        self.col = col
        self.level = level


class Solution:
    def verticalTraversalBFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        tree_map = defaultdict(list)
        queue = deque([Triplet(root, 0, 0)])
        while queue:
            for _ in range(len(queue)):
                triplet = queue.popleft()
                tree_map[triplet.col].append(triplet)

                if triplet.node.left:
                    queue.append(Triplet(triplet.node.left, triplet.col - 1, triplet.level + 1))

                if triplet.node.right:
                    queue.append(Triplet(triplet.node.right, triplet.col + 1, triplet.level + 1))

        for col in sorted(tree_map.keys()):
            triplet_list = tree_map[col]
            triplet_list.sort(key=lambda x: (x.level, x.node.val))
            result.append([triplet.node.val for triplet in triplet_list])
        return result

    def verticalTraversal_DFS1(self, root: TreeNode) -> List[List[int]]:
        # Traverse the tree and store each node's value along with its position (level and vertical distance from root)
        def dfs(node, level, col):
            if not node:
                return
            nodes.append((level, col, node.val))
            dfs(node.left, level + 1, col - 1)  # Traverse left with increased level and decreased vertical distance
            dfs(node.right, level + 1, col + 1)  # Traverse right with increased level and increased vertical distance

        nodes = []
        dfs(root, 0, 0)

        # Sort the nodes firstly by vertical distance, then by level, and finally by the node's value
        nodes.sort(key=lambda x: (x[1], x[0], x[2]))

        # Group the nodes by their vertical distance
        result = []
        prev_vertical_distance = float('-inf')  # Initialize with negative infinity (to ensure the first vertical distance is different)

        for level, vertical_distance, value in nodes:
            if prev_vertical_distance != vertical_distance:
                # Start a new grouping when the vertical distance changes
                result.append([])
                prev_vertical_distance = vertical_distance
            result[-1].append(value)  # Add the current node's value to the current vertical grouping

        return result

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # Traverse the tree and store each node's value along with its position (level and vertical distance from root)
        def dfs(node, level, col):
            if not node:
                return
            vertical_map[col].append((level, node.val))
            dfs(node.left, level + 1, col - 1)  # Traverse left with increased level and decreased vertical distance
            dfs(node.right, level + 1, col + 1)  # Traverse right with increased level and increased vertical distance

        vertical_map = defaultdict(list)
        dfs(root, 0, 0)

        result = []

        for col in sorted(vertical_map.keys()):
            column_nodes = sorted(vertical_map[col])
            #column_nodes = sorted(vertical_map[col], key=lambda x: (x[0], x[1])) here lambda is optional
            result.append([val for _, val in column_nodes])
        return result

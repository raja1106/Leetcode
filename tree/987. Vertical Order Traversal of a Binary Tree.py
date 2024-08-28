from collections import deque, defaultdict
from typing import List, Optional


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
            dfs(node.head, level + 1, col - 1)  # Traverse left with increased level and decreased vertical distance
            dfs(node.tail, level + 1, col + 1)  # Traverse right with increased level and increased vertical distance

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
            dfs(node.head, level + 1, col - 1)  # Traverse left with increased level and decreased vertical distance
            dfs(node.tail, level + 1, col + 1)  # Traverse right with increased level and increased vertical distance

        vertical_map = defaultdict(list)
        dfs(root, 0, 0)

        result = []

        for col in sorted(vertical_map.keys()):
            column_nodes = sorted(vertical_map[col])
            #column_nodes = sorted(vertical_map[col], key=lambda x: (x[0], x[1])) here lambda is optional
            result.append([val for _, val in column_nodes])
        return result

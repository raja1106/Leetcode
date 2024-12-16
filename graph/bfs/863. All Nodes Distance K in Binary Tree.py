from collections import defaultdict, deque
from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Build the graph representation of the binary tree
        graph = defaultdict(list)

        def build_graph(node):
            if not node:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                build_graph(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                build_graph(node.right)

        build_graph(root)

        # BFS to find all nodes at distance K
        queue = deque([(target.val, 0)])  # Start from the target node
        visited = set([target.val])  # Track visited nodes
        result = []

        while queue:
            current_node, distance = queue.popleft()

            # If we reach distance K, add to result
            if distance == k:
                result.append(current_node)
                continue

            # Otherwise, explore neighbors
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        return result

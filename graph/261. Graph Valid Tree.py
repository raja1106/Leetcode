from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # Build the graph as an adjacency list
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        visited = set()

        # DFS function with parent tracking for cycle detection
        def dfs(node, parent):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:  # Visit unvisited neighbors
                    if not dfs(neighbour, node):  # If a cycle is detected, return False
                        return False
                elif neighbour != parent:  # Cycle detected
                    return False
            return True

        # Check if the graph is connected and has no cycles
        # Start DFS from node 0
        if not dfs(0, -1):  # -1 as the parent of the root
            return False

        # Ensure all nodes are visited (graph is connected)
        return len(visited) == n
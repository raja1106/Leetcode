
from typing import List
from collections import defaultdict, deque

class Solution_Topoogical_Sort_best_one:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        # Step 1: Build reverse graph and calculate out-degrees
        reverse_graph = defaultdict(list)
        out_degree = [0] * n

        for src in range(n):
            for dst in graph[src]:
                reverse_graph[dst].append(src)
            out_degree[src] = len(graph[src])

        # Step 2: Initialize queue with terminal nodes (nodes with 0 out-degree)
        queue = deque([i for i in range(n) if out_degree[i] == 0])
        safe = [False] * n

        # Step 3: Topological sort using Kahn's algorithm on reversed graph
        while queue:
            node = queue.popleft()
            safe[node] = True
            for parent in reverse_graph[node]:
                out_degree[parent] -= 1
                if out_degree[parent] == 0:
                    queue.append(parent)

        # Step 4: Collect all safe nodes
        return sorted([i for i in range(n) if safe[i]])

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n  # 0 = unvisited, 1 = visiting, 2 = safe

        def dfs(node):
            if state[node] > 0:
                return state[node] == 2  # Return True if the node is safe

            # Mark the node as visiting (part of the current DFS path)
            state[node] = 1

            # Visit all neighbors
            for neighbor in graph[node]:
                if not dfs(neighbor):  # If any neighbor is not safe, the current node is not safe
                    return False

            # If all neighbors are safe, mark the current node as safe
            state[node] = 2
            return True

        # Run DFS for each node
        result = [i for i in range(n) if dfs(i)]

        return result

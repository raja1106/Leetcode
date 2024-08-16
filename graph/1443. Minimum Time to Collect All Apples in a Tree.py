from typing import List
from collections import defaultdict


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Build the adjacency list representation of the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # DFS function to calculate the minimum time
        def dfs(node: int, parent: int) -> int:
            total_time = 0
            # Traverse all the children of the current node
            for child in graph[node]:
                if child == parent:
                    continue
                # Recursively calculate the time for the subtree
                time_from_child = dfs(child, node)
                if time_from_child > 0 or hasApple[child]:
                    total_time += time_from_child + 2

            return total_time

        # Start DFS from the root node (0) with no parent (-1)
        return dfs(0, -1)

sol = Solution()
n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False, False, True, False, True, True, False]
print(sol.minTime(n, edges, hasApple))  # Output should be 8

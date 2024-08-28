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


class Solution_Algo:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Helper function to perform depth-first search from the current node.
        # Construct the graph using adjacency lists.
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # Initialize a visited list to avoid revisiting nodes.
        visited = [False] * n
        def dfs(current_node, cost_to_come_back):
            # If the current node has been visited, no need to do anything.
            if visited[current_node]:
                return 0
            visited[current_node] = True

            # Accumulated cost of visiting children nodes.
            total_cost = 0
            for child_node in graph[current_node]:
                # Perform DFS on child nodes with the cost of coming back (2 units).
                total_cost += dfs(child_node, 2)
            # If there's no apple at the current node, and no cost accumulated from children,
            # it means we don't need to collect any apples on this path.
            if not hasApple[current_node] and total_cost == 0:
                return 0
            # Return the total cost of picking apples from this subtree (including the cost to come back).
            return cost_to_come_back + total_cost

        # Perform a DFS starting at node 0 with no initial cost.
        # Since we start at the root and don't need to return, we pass 0 as the cost.
        return dfs(0, 0)


sol = Solution()
n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
hasApple = [False, False, True, False, True, True, False]
print(sol.minTime(n, edges, hasApple))  # Output should be 8

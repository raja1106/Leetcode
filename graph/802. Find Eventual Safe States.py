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

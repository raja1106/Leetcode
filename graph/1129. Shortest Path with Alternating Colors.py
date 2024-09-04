from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        # Create adjacency lists for red and blue edges
        graph = [defaultdict(list) for _ in range(2)]
        for src, dst in redEdges:
            graph[0][src].append(dst)
        for src, dst in blueEdges:
            graph[1][src].append(dst)

        # Initialize distances: res[0] for red, res[1] for blue
        res = [[float('inf')] * n for _ in range(2)]
        res[0][0] = res[1][0] = 0  # Distance to start node is 0 for both colors

        # BFS queue: (node, color), where color is 0 (red) or 1 (blue)
        queue = deque([(0, 0), (0, 1)])  # Start with both red and blue edges from node 0

        while queue:
            node, color = queue.popleft()
            next_color = 1 - color  # Alternate color
            for neighbor in graph[next_color][node]:
                if res[next_color][neighbor] == float('inf'):
                    res[next_color][neighbor] = res[color][node] + 1
                    queue.append((neighbor, next_color))

        # Build the final answer
        answer = []
        for i in range(n):
            shortest = min(res[0][i], res[1][i])
            answer.append(shortest if shortest != float('inf') else -1)

        return answer

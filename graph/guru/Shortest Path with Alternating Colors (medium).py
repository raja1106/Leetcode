from collections import deque, defaultdict


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        # Create adjacency lists for red and blue edges
        graph = [defaultdict(list) for _ in range(2)]
        for u, v in redEdges:
            graph[0][u].append(v)
        for u, v in blueEdges:
            graph[1][u].append(v)

        # Initialize the result array with max values
        res = [[float('inf')] * n for _ in range(2)]
        res[0][0] = res[1][0] = 0  # Starting node has distance 0

        # Perform BFS for both red and blue edges starting from node 0
        self.bfs(0, 0, graph, res, n)  # Start with red
        self.bfs(0, 1, graph, res, n)  # Start with blue

        # Fill the answer array with the shortest paths
        answer = []
        for i in range(n):
            shortest = min(res[0][i], res[1][i])
            answer.append(shortest if shortest != float('inf') else -1)

        return answer

    def bfs(self, source, color, graph, res, n):
        # Template BFS adjusted for alternating paths
        queue = deque([(source, color)])
        while queue:
            node, color = queue.popleft()
            for neighbor in graph[1 - color][node]:
                if res[1 - color][neighbor] == float('inf'):
                    res[1 - color][neighbor] = res[color][node] + 1
                    queue.append((neighbor, 1 - color))

# Test Case 1: Minimal input with no edges
n1 = 1
redEdges1 = []
blueEdges1 = []
expected1 = [0]
#print(Solution().shortestAlternatingPaths(n1, redEdges1, blueEdges1))  # Expected: [0]

# Test Case 2: Only red edges, no blue edges
n2 = 3
redEdges2 = [[0, 1], [1, 2]]
blueEdges2 = []
expected2 = [0, 1, 2]
print(Solution().shortestAlternatingPaths(n2, redEdges2, blueEdges2))  # Expected: [0, 1, 2]

# Test Case 3: Only blue edges, no red edges
n3 = 3
redEdges3 = []
blueEdges3 = [[0, 1], [1, 2]]
expected3 = [0, 1, 2]
print(Solution().shortestAlternatingPaths(n3, redEdges3, blueEdges3))  # Expected: [0, 1, 2]

# Test Case 4: Mixed edges with alternating paths
n4 = 3
redEdges4 = [[0, 1]]
blueEdges4 = [[1, 2]]
expected4 = [0, 1, 2]
print(Solution().shortestAlternatingPaths(n4, redEdges4, blueEdges4))  # Expected: [0, 1, 2]

# Test Case 5: Disconnected graph
n5 = 4
redEdges5 = [[0, 1]]
blueEdges5 = [[2, 3]]
expected5 = [0, 1, -1, -1]
print(Solution().shortestAlternatingPaths(n5, redEdges5, blueEdges5))  # Expected: [0, 1, -1, -1]

# Test Case 6: Multiple shortest paths
n6 = 5
redEdges6 = [[0, 1], [0, 2], [2, 4]]
blueEdges6 = [[1, 2], [2, 3], [3, 4]]
expected6 = [0, 1, 1, 2, 2]
print(Solution().shortestAlternatingPaths(n6, redEdges6, blueEdges6))  # Expected: [0, 1, 1, 2, 2]

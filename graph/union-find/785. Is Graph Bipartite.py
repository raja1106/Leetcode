from typing import List


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size
        self.components = size

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by size
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            self.components -= 1

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        uf = UnionFind(n)

        # Iterate through each node
        for node in range(n):
            # Iterate through its neighbors
            for neighbor in graph[node]:
                # If the node and its neighbor have the same root, it's not bipartite
                if uf.find(node) == uf.find(neighbor):
                    return False
                # Union the node with one of its neighbors' neighbors
                # Ensure all neighbors are in a different set from the node
                uf.union(graph[node][0], neighbor)

        return True


from typing import List
from collections import deque


class Solution_BFS:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # -1 means unvisited

        for start_node in range(n):
            if color[start_node] == -1:
                queue = deque([start_node])
                color[start_node] = 0  # Start with color 0
                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if color[neighbor] == -1:
                            color[neighbor] = 1 - color[node]  # Assign opposite color
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:
                            return False  # Conflict detected
        return True

from collections import defaultdict
from collections import defaultdict

'''
For Linear graph, there is always possible for Bipartition and it is always True. 
Only if it is having Cycle, it is True for even length cycle and False for Odd Cycle
'''
class Solution_2026:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        # form a graph
        graph = defaultdict(list)

        for src, dst in dislikes:
            graph[src].append(dst)
            graph[dst].append(src)
        queue = collections.deque()
        colors = [0] * (n + 1)  # 0 is no color, -1 is groupA,1 is groupB

        def bfs(start_node):
            colors[start_node] = -1
            queue.append(start_node)

            while queue:
                node = queue.popleft()

                for neighbour in graph[node]:
                    if colors[neighbour] == 0:
                        colors[neighbour] = -colors[node]
                        queue.append(neighbour)
                    elif colors[neighbour] == colors[node]:
                        return False

            return True

        for node in range(1, n + 1):
            if colors[node] == 0 and not bfs(node):
                return False

        return True

from typing import List
from collections import deque, defaultdict

class Solution_BFS:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # Step 1: Build the undirected graph (1-based indexing)
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Apply BFS-based 2-coloring
        color = [-1] * (n+1)  # -1 means unvisited

        for start_node in range(1,n+1):
            if color[start_node] == -1:
                queue = deque([start_node])
                color[start_node] = 0  # Start with color 0

                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if color[neighbor] == -1:
                            color[neighbor] = 1 - color[node]
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:
                            return False  # Conflict detected

        return True

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size)) # [0,1,2,3,1,5]
        self.size = [1] * size  #[1,1,1,1,1,1]
        self.components = size #5

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x) # 1
        rootY = self.find(y) # 2

        if rootX != rootY:
            # Union by size
            if self.size[rootX] < self.size[rootY]: #rooty- admk(100), rootx -bjp(25)
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            self.components -= 1

class Solution:
    def possibleBipartition(self, n, dislikes):
        graph = defaultdict(list)  # Create adjacency list for dislikes
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        uf = UnionFind(n + 1)  # Initialize UnionFind structure
        for node in range(1, n + 1):
            if not graph[node]:
                continue  # Skip if the node has no dislikes
            for neighbor in graph[node]:
                if uf.find(node) == uf.find(neighbor):
                    return False  # If they are in the same set, return false
                uf.union(graph[node][0], neighbor)  # Union all neighbors into the same set as the first neighbor
        return True  # If no conflicts, return true

# Test cases
sol = Solution()
print(sol.possibleBipartition(5, [[1, 2], [2, 3], [3, 4], [4, 5]]))  # true
print(sol.possibleBipartition(6, [[1, 2], [2, 4], [4, 6], [4, 5], [5, 6]]))  # false
print(sol.possibleBipartition(3, [[1, 2], [1, 3]]))  # true

from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  # Initialize parent array
        self.rank = [0] * size  # Initialize rank array

    def find(self, x):
        #return root as usual after doing path compression
        #Base case
        if x == self.parent[x]:
            return x
        #Recursive case
        root_x = self.find(self.parent[x])  # Path compression
        self.parent[x] = root_x
        return root_x

    def union(self, x, y):
        rootX = self.find(x)  # Find root of x
        rootY = self.find(y)  # Find root of y
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX  # Union by rank
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY  # Union by rank
            else:
                self.parent[rootY] = rootX  # Union by rank
                self.rank[rootX] += 1  # Increment rank if ranks are equal
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
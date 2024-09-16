from typing import List


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
from collections import defaultdict
from typing import List

#Not able to understand the problem now. Will look into this later.
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  # Initialize parent array
        self.rank = [0] * size  # Initialize rank array
        self.components = size  # Number of connected components
    def find(self, x):
        # return root as usual after doing path compression
        # Base case
        if x == self.parent[x]:
            return x
        # Recursive case
        root_x = self.find(self.parent[x])  # Path compression
        self.parent[x] = root_x
        return root_x
    def union(self, x, y):
        rootX = self.find(x)  # Find root of x
        rootY = self.find(y)  # Find root of y

        if rootX != rootY:
            # Union by size: Attach the smaller tree under the larger tree
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]  # Update the size of rootY
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]  # Update the size of rootX
            # Decrease the number of components after a successful union
            self.components -= 1



class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)

        # Step 1: Union all pairs to identify connected components
        for a, b in pairs:
            uf.union(a, b)

        # Step 2: Group characters by their connected components
        components = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            components[root].append(i)

        # Step 3: Sort characters within each component and reconstruct the string
        s_list = list(s)
        for indices in components.values():
            # Sort the characters and the indices, and reassign them in lexicographical order
            chars = sorted(s_list[i] for i in indices)
            for i, char in zip(sorted(indices), chars):
                s_list[i] = char

        return ''.join(s_list)
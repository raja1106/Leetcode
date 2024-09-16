from collections import defaultdict
from typing import List

#Not able to understand the problem now. Will look into this later.
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

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
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


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
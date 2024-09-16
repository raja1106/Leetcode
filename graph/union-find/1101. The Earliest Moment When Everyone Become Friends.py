from collections import defaultdict
from typing import List


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
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            # Decrease the number of components after a successful union
            self.components -= 1


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # Sort logs by the timestamp
        logs.sort(key=lambda x: x[0])

        # Initialize UnionFind for n people
        uf = UnionFind(n)

        # Process each log and union the individuals
        for time, src, dst in logs:
            uf.union(src, dst)

            # If all individuals are connected (only 1 component remains)
            if uf.components == 1:
                return time

        # If we never achieve full connection, return -1
        return -1


logs = [[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3], [20190211, 1, 5], [20190224, 2, 4], [20190301, 0, 3],
        [20190312, 1, 2], [20190322, 4, 5]]
n = 6

sol = Solution()
print(sol.earliestAcq(logs, n))

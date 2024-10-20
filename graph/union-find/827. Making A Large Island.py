from typing import List
from collections import deque


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size  # Initialize size of each component to 1
        self.components = size  # Number of connected components

    def find(self, x):
        # Path compression
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by size (attach the smaller tree under the larger tree)
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            self.components -= 1

    def get_size(self, x):
        root = self.find(x)
        return self.size[root]


class Solution_UnionFind_Approach:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(n * n)

        def index(r, c):
            return r * n + c

        # Step 1: Union adjacent land cells (1's) using UnionFind
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    for nr, nc in [(r + 1, c), (r, c + 1)]:  # Check right and down
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            uf.union(index(r, c), index(nr, nc))

        # Step 2: Check for the largest island
        max_island = max(uf.size)  # Initial largest island size

        # Step 3: Try flipping each 0 to 1 and calculate the possible island size
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen_components = set()
                    island_size = 1  # This cell itself is now land

                    for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            root = uf.find(index(nr, nc))
                            if root not in seen_components:
                                island_size += uf.get_size(root)
                                seen_components.add(root)

                    max_island = max(max_island, island_size)

        return max_island if max_island != 0 else n * n  # If grid is all 1's, return the total area


# Example usage:
# grid = [[1, 0], [0, 1]]
# sol = Solution()
# print(sol.largestIsland(grid))  # Output would be 3 by flipping one 0 to 1

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def bfs(x, y, index):
            queue = deque([(x, y)])
            area = 0
            while queue:
                i, j = queue.popleft()
                if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                    grid[i][j] = index
                    area += 1
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            queue.append((ni, nj))
            return area

        n = len(grid)
        if n == 0:
            return 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        island_sizes = {}
        index = 2

        # Step 1: Identify and label all islands with their sizes using BFS
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_sizes[index] = bfs(i, j, index)
                    index += 1

        # If the whole grid is an island
        max_area = max(island_sizes.values(), default=0)

        # Step 2: Check each 0 and calculate the potential island size if it is flipped
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    area = 1  # 1 for the flip itself
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            idx = grid[ni][nj]
                            if idx not in seen:
                                seen.add(idx)
                                area += island_sizes[idx]
                    max_area = max(max_area, area)

        return max_area

# Example usage:
# grid = [[1, 0], [0, 1]]
# sol = Solution()
# print(sol.largestIsland(grid))  # Output: 3

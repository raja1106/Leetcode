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
                    visited = set()
                    island_size = 1  # This cell itself is now land

                    for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            root = uf.find(index(nr, nc))
                            if root not in visited:
                                island_size += uf.get_size(root)
                                visited.add(root)

                    max_island = max(max_island, island_size)

        return max_island


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
                    visited = set()
                    area = 1  # 1 for the flip itself
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            idx = grid[ni][nj]
                            if idx not in visited:
                                visited.add(idx)
                                area += island_sizes[idx]
                    max_area = max(max_area, area)

        return max_area

# Example usage:
# grid = [[1, 0], [0, 1]]
# sol = Solution()
# print(sol.largestIsland(grid))  # Output: 3
from typing import List

class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.size = [1] * size  # Size of each component
        self.components = size

    def find(self, x: int) -> int:
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return
        # Union by size: attach smaller tree under larger
        if self.size[rootX] < self.size[rootY]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
        self.components -= 1

    def get_size(self, x: int) -> int:
        return self.size[self.find(x)]

class Solution_Union_Find_Easy_To_understand:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(n * n)

        def index(r, c):
            return r * n + c

        # Step 1: Union all adjacent land cells (1s)
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    for dr, dc in [(1, 0), (0, 1)]:  # Down and Right
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            uf.union(index(r, c), index(nr, nc))

        # Step 2: Compute the initial max island size without flipping
        max_island = max(uf.size) if any(1 in row for row in grid) else 0

        # Step 3: Try flipping each 0 to 1 and compute possible island size
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    size = 1  # This flipped cell

                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            root = uf.find(index(nr, nc))
                            if root not in seen:
                                seen.add(root)
                                size += uf.get_size(root)

                    max_island = max(max_island, size)

        return max_island
from typing import List
from collections import deque

class Solution_Best_BFS:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        island_sizes = {}  # island id -> size
        island_id = 2  # start from 2 since 0 and 1 are used

        # Step 1: BFS to label each island with a unique id and store its size
        def bfs(r: int, c: int, island_id: int) -> int:
            queue = deque([(r, c)])
            grid[r][c] = island_id
            size = 1

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = island_id
                        size += 1
                        queue.append((nx, ny))
            return size

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size = bfs(r, c, island_id)
                    island_sizes[island_id] = size
                    island_id += 1

        # If the entire grid is already land
        max_island = max(island_sizes.values(), default=0)

        # Step 2: Try flipping each 0 to 1 and compute max possible island
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    total = 1  # include flipped cell
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy
                        if 0 <= nr < n and 0 <= nc < n:
                            island = grid[nr][nc]
                            if island > 1 and island not in seen:
                                total += island_sizes[island]
                                seen.add(island)
                    max_island = max(max_island, total)

        return max_island if max_island > 0 else 1

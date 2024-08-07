from typing import List
from collections import deque


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

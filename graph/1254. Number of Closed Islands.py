from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # Helper function to perform DFS
        def dfs(x: int, y: int):
            grid[x][y] = 1
            for dr, dc in directions:
                nr, nc = x + dr, y + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    dfs(nr, nc)

        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # grid consists of 0s (land) and 1s (water).
        # Step 1: Flood-fill all islands connected to the boundary
        for i in range(rows):
            for j in [0, cols - 1]:  # Only look at the first and last columns
                if grid[i][j] == 0:
                    dfs(i, j)
        for j in range(cols):
            for i in [0, rows - 1]:  # Only look at the first and last rows
                if grid[i][j] == 0:
                    dfs(i, j)

        # Step 2: Count the number of closed islands
        closed_islands = 0
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if grid[i][j] == 0:
                    closed_islands += 1
                    dfs(i, j)  # Flood-fill the closed island
        return closed_islands

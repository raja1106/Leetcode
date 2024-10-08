from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row: int, col: int) -> int:
            # Mark the current cell as visited
            grid[row][col] = None
            area = 1  # Start with the current cell

            # Explore all four directions
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < num_rows and 0 <= nc < num_cols and grid[nr][nc] == 1:
                    area += dfs(nr, nc)
            return area

        def bfs(r, c):
            queue = deque()
            area = 1
            grid[r][c] = 2
            queue.append((r, c))
            while queue:
                current_row, current_col = queue.popleft()
                for dr, dc in directions:
                    nr = current_row + dr
                    nc = current_col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = '2'
                        area += 1
                        queue.append((nr, nc))
            return area

        if not grid or not grid[0]:
            return 0

        num_rows, num_cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_island_area = 0

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    # Compute the area of the island using DFS
                    island_area = dfs(row, col)
                    # Update the maximum area found
                    max_island_area = max(max_island_area, island_area)

        return max_island_area

class Solution_Naive:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1 ,0) ,(-1 ,0) ,(0 ,1) ,(0 ,-1)]
        rows ,cols = len(grid) ,len(grid[0])
        max_area = 0
        current_seq = 0
        def dfs(r ,c):
            nonlocal current_seq
            grid[r][c] = None

            for dr ,dc in directions:
                nr ,nc = r+ dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    current_seq += 1
                    dfs(nr, nc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    current_seq = 1
                    dfs(row, col)
                    max_area = max(max_area, current_seq)
                    current_seq = 0

        return max_area
from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        # Initialize the queue with all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh_count += 1
        # Directions for moving in the grid (right, left, down, up)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        time_elapsed = 0
        # Perform BFS
        while queue:
            r, c, time = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc, time + 1))
                    time_elapsed = time + 1
        # If there are still fresh oranges left, return -1
        if fresh_count > 0:
            return -1
        return time_elapsed

# Example usage:
# sol = Solution()
# print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))  # Output: 4

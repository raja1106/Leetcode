from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # If the start or end point is blocked, no path can exist.
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        # Get the number of rows and columns.
        num_rows = len(grid)
        num_cols = len(grid[0])
        # Define possible 8-directional movements (horizontal, vertical, diagonal).
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        # Initialize the BFS queue with the start point (0, 0) and the path length of 1.
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1  # Mark the start cell as visited.

        # Perform BFS to explore the grid.
        while queue:
            r, c, path_length = queue.popleft()

            # If we've reached the bottom-right corner, return the path length.
            if r == num_rows - 1 and c == num_cols - 1:
                return path_length

            # Explore all possible 8 directions from the current cell.
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check if the new position is within bounds and not visited.
                if 0 <= nr < num_rows and 0 <= nc < num_cols and grid[nr][nc] == 0:
                    grid[nr][nc] = 1  # Mark the new cell as visited.
                    queue.append((nr, nc, path_length + 1))
        # If no path is found, return -1.
        return -1

from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        start_row, start_col = entrance[0], entrance[1]
        rows, cols = len(maze), len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        queue.append((start_row, start_col, 0))

        # Mark the entrance as visited to prevent revisiting it
        maze[start_row][start_col] = '+'

        while queue:
            row, col, steps = queue.popleft()

            # Check if this is an exit (and not the entrance)
            if (steps > 0) and (row == 0 or row == rows - 1 or col == 0 or col == cols - 1):
                return steps

            # Explore all 4 directions
            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                # Only add unvisited cells to the queue
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
                    queue.append((nr, nc, steps + 1))
                    # Mark it as visited when it's added to the queue
                    maze[nr][nc] = '+'

        return -1

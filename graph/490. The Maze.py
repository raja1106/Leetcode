from collections import deque
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # If the destination is blocked, return False
        if maze[destination[0]][destination[1]] == 1:
            return False

        # Possible movement directions: down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Initialize BFS queue and visited set
        queue = deque([(start[0], start[1])])  # Store (row, col)
        visited = set()  # Track visited positions
        visited.add((start[0], start[1]))

        num_rows, num_cols = len(maze), len(maze[0])

        # Perform BFS
        while queue:
            r, c = queue.popleft()

            # Check if the destination is reached
            if [r, c] == destination:
                return True

            # Explore all four possible directions
            for dr, dc in directions:
                nr, nc = r, c

                # Keep rolling in the direction until hitting a wall or boundary
                while 0 <= nr + dr < num_rows and 0 <= nc + dc < num_cols and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc

                # If the new position has not been visited, add it to the queue
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        # If no path is found, return False
        return False

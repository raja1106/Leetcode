from typing import List
import collections


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # DFS to mark the first island and add its boundary points to the queue
        def dfs(row, col):
            grid[row][col] = -1  # Mark the current cell as visited (part of the first island)
            for delta_row, delta_col in directions:
                next_row, next_col = row + delta_row, col + delta_col
                if 0 <= next_row < total_rows and 0 <= next_col < total_cols:
                    if grid[next_row][next_col] == 0:  # If it's water, mark as boundary
                        grid[next_row][next_col] = -1
                        queue.append((next_row, next_col, 1))  # Add boundary point to the queue with distance 1
                    elif grid[next_row][next_col] == 1:  # If it's part of the island, continue DFS
                        dfs(next_row, next_col)

        queue = collections.deque()
        total_rows, total_cols = len(grid), len(grid[0])
        is_first_island_found = False

        # Step 1: Find the first island and mark it using DFS
        for row in range(total_rows):
            if is_first_island_found:
                break
            for col in range(total_cols):
                if grid[row][col] == 1:
                    dfs(row, col)  # DFS to mark the first island
                    is_first_island_found = True
                    break

        # Step 2: Perform BFS from the boundary of the first island to find the shortest path to the second island
        while queue:
            curr_row, curr_col, distance = queue.popleft()
            for delta_row, delta_col in directions:
                next_row, next_col = curr_row + delta_row, curr_col + delta_col
                if 0 <= next_row < total_rows and 0 <= next_col < total_cols:
                    if grid[next_row][next_col] == 0:  # If it's water, continue expanding the bridge
                        grid[next_row][next_col] = -1  # Mark as visited
                        queue.append((next_row, next_col, distance + 1))
                    elif grid[next_row][next_col] == 1:  # Found the second island
                        return distance  # Return the shortest bridge distance

        return -1  # If no bridge is found (though the problem guarantees a solution)

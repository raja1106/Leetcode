from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        m, n = len(grid), len(grid[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        grid[0][0] = 1  # Mark as visited

        while queue:
            x, y, length = queue.popleft()
            if x == m - 1 and y == n - 1:
                return length

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                    queue.append((nx, ny, length + 1))
                    grid[nx][ny] = 1  # Mark as visited

        return -1


# Example usage:
solution = Solution()
grid1 = [[0, 1], [1, 0]]
print(solution.shortestPathBinaryMatrix(grid1))  # Output: 2

grid2 = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
print(solution.shortestPathBinaryMatrix(grid2))  # Output: 4

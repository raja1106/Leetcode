from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()

        # Initialize the result matrix with -1 and enqueue all cells containing 0
        updated_matrix = [[-1] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    updated_matrix[row][col] = 0
                    queue.append((row, col))

        # Perform BFS from all 0s simultaneously
        while queue:
            current_row, current_col = queue.popleft()

            # Explore all 4 directions
            for dr, dc in directions:
                nr, nc = current_row + dr, current_col + dc
                if 0 <= nr < rows and 0 <= nc < cols and updated_matrix[nr][nc] == -1:
                    updated_matrix[nr][nc] = updated_matrix[current_row][current_col] + 1
                    queue.append((nr, nc))

        return updated_matrix


class Solution_DP:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dp = [row[:] for row in mat]
        m, n = len(dp), len(dp[0])

        for row in range(m):
            for col in range(n):
                min_neighbor = inf
                if dp[row][col] != 0:
                    if row > 0:
                        min_neighbor = min(min_neighbor, dp[row - 1][col])
                    if col > 0:
                        min_neighbor = min(min_neighbor, dp[row][col - 1])

                    dp[row][col] = min_neighbor + 1

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                min_neighbor = inf
                if dp[row][col] != 0:
                    if row < m - 1:
                        min_neighbor = min(min_neighbor, dp[row + 1][col])
                    if col < n - 1:
                        min_neighbor = min(min_neighbor, dp[row][col + 1])

                    dp[row][col] = min(dp[row][col], min_neighbor + 1)

        return dp

class Solution_MySolution:
    # This was not efficient as T(n) = O((rows×cols)^2)
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        def bfs(row, col):
            queue = collections.deque([(row, col, 1)])

            while queue:
                current_row, current_col, level = queue.popleft()
                for dr, dc in directions:
                    nr, nc = current_row + dr, current_col + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if mat[nr][nc] == 0:
                            return level
                        elif mat[nr][nc] == 1:
                            queue.append((nr, nc, level + 1))
            return -1

        updated_matrix = [[-1] * cols for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    updated_matrix[row][col] = 0
                else:
                    updated_matrix[row][col] = bfs(row, col)

        return updated_matrix







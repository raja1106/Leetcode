from collections import deque
from typing import List

from collections import deque
from typing import List


class Solution_Best_One_May_2025:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        distance_matrix = [[-1] * cols for _ in range(rows)]
        queue = deque()
        ones_remaining = 0

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    distance_matrix[row][col] = 0
                    queue.append((row, col, 0))  # (row, col, distance)
                else:
                    ones_remaining += 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

        while queue and ones_remaining > 0:
            current_row, current_col, current_distance = queue.popleft()

            for delta_row, delta_col in directions:
                neighbor_row = current_row + delta_row
                neighbor_col = current_col + delta_col

                if (
                        0 <= neighbor_row < rows and
                        0 <= neighbor_col < cols and
                        distance_matrix[neighbor_row][neighbor_col] == -1
                ):
                    queue.append((neighbor_row, neighbor_col, current_distance + 1))
                    distance_matrix[neighbor_row][neighbor_col] = current_distance + 1
                    ones_remaining -= 1

        return distance_matrix


class Solution_Without_Having_Extra_memory:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()

        # Initialize the result matrix with -1 and enqueue all cells containing 0
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    mat[row][col] = 0
                    queue.append((row, col))
                else:
                    mat[row][col] = -1

        # Perform BFS from all 0s simultaneously
        while queue:
            current_row, current_col = queue.popleft()

            # Explore all 4 directions
            for dr, dc in directions:
                nr, nc = current_row + dr, current_col + dc
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[current_row][current_col] + 1
                    queue.append((nr, nc))

        return mat
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







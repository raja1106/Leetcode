class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(grid)
        cols = len(grid[0])

        ans_count = 0
        boundery_set = set()

        def bfs(r, c):
            queue = deque()
            visited = set()
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                current_row, current_col = queue.popleft()
                if current_row in (0, rows - 1) or current_col in (0, cols - 1):
                    boundery_set.update(visited)
                    return True
                for dr, dc in directions:
                    nr, nc = dr + current_row, dc + current_col

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))

            return False

        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                if grid[row][col] == 1 and (row, col) not in boundery_set:
                    if not bfs(row, col):
                        ans_count += 1

        return ans_count


from collections import deque
from typing import List


class Solution_GPT:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            is_boundary = False
            region_size = 0

            while queue:
                row, col = queue.popleft()
                region_size += 1

                if row in (0, rows - 1) or col in (0, cols - 1):
                    is_boundary = True

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (
                            0 <= nr < rows and
                            0 <= nc < cols and
                            grid[nr][nc] == 1 and
                            (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return 0 if is_boundary else region_size

        enclave_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    enclave_count += bfs(r, c)

        return enclave_count

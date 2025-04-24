class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(matrix), len(matrix[0])
        memo = {}
        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            longest_neighbor_seq = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    longest_neighbor_seq = max(longest_neighbor_seq, dfs(nr, nc))
            memo[(r, c)] = 1 + longest_neighbor_seq
            return 1 + longest_neighbor_seq

        global_max = 1
        for i in range(m):
            for j in range(n):
                local_seq = dfs(i, j)
                global_max = max(global_max, local_seq)

        return global_max

class Solution_Topological_sort:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:  # Edge case handling
            return 0

        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Step 1: Compute in-degrees (count of incoming edges for each cell)
        in_degree = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                        in_degree[nr][nc] += 1

        # Step 2: Initialize BFS queue with all cells having in-degree = 0
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if in_degree[r][c] == 0:
                    queue.append((r, c))

        # Step 3: Process BFS in levels (each level represents an increasing path length)
        max_length = 0
        while queue:
            max_length += 1
            for _ in range(len(queue)):  # Process all nodes in the current level
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                        in_degree[nr][nc] -= 1
                        if in_degree[nr][nc] == 0:
                            queue.append((nr, nc))

        return max_length


from collections import deque


class Solution_BFS_April_2025:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        longest_increasing_path = 0
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        memo = {}
        def find_longest_increasing_path(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            nonlocal longest_increasing_path
            local_increasing_path = 0
            seen = set()
            seen.add((row, col))
            queue = deque()
            queue.append((matrix[row][col], 1, row, col))
            while queue:
                current_val, current_seq, current_row, current_col = queue.popleft()
                local_increasing_path = max(current_seq, local_increasing_path)
                for dr, dc in directions:
                    new_row = current_row + dr
                    new_col = current_col + dc
                    if 0 <= new_row < num_rows and 0 <= new_col < num_cols and matrix[new_row][new_col] > current_val:
                        seen.add((new_row, new_col))
                        queue.append((matrix[new_row][new_col], current_seq + 1, new_row, new_col))
            memo[(row, col)] = local_increasing_path
            longest_increasing_path = max(longest_increasing_path, local_increasing_path)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                find_longest_increasing_path(i, j)
        return longest_increasing_path

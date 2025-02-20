class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp_table = [[0] * cols for _ in range(rows)]
        dp_table[0][0] = grid[0][0]
        for row in range(1, rows):
            dp_table[row][0] = dp_table[row - 1][0] + grid[row][0]
        for col in range(1, cols):
            dp_table[0][col] = dp_table[0][col - 1] + grid[0][col]

        for row in range(1, rows):
            for col in range(1, cols):
                dp_table[row][col] = min(dp_table[row - 1][col], dp_table[row][col - 1]) + grid[row][col]

        return dp_table[rows - 1][cols - 1]


class Solution_Space_Optimization:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [0] * cols

        dp[0] = grid[0][0]

        # Initialize the first row
        for col in range(1, cols):
            dp[col] = dp[col - 1] + grid[0][col]

        # Update the dp array for each subsequent row
        for row in range(1, rows):
            dp[0] += grid[row][0]  # Update the first column for the current row
            for col in range(1, cols):
                dp[col] = min(dp[col], dp[col - 1]) + grid[row][col]

        return dp[-1]
from typing import List

class Solution_Memo:
    def minPathSum(self, grid: List[List[int]]) -> int:
        min_sum = float('inf')
        m, n = len(grid), len(grid[0])
        memo = {}

        def dfs(i, j, current_sum):
            nonlocal min_sum

            # Base case: reached bottom-right cell
            if i == m - 1 and j == n - 1:
                min_sum = min(min_sum, current_sum)
                return

            # Check memoization
            if (i, j) in memo and memo[(i, j)] <= current_sum:
                return  # Avoid unnecessary calls

            memo[(i, j)] = current_sum

            # Move Down
            if i + 1 < m:
                dfs(i + 1, j, current_sum + grid[i + 1][j])
            # Move Right
            if j + 1 < n:
                dfs(i, j + 1, current_sum + grid[i][j + 1])

        dfs(0, 0, grid[0][0])
        return min_sum


from typing import List


class Solution_Memo2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}

        def dfs(i, j):
            # Base case: Reached bottom-right cell
            if i == m - 1 and j == n - 1:
                return grid[i][j]

            # Check if already computed
            if (i, j) in memo:
                return memo[(i, j)]

            # Move right and down
            right = dfs(i, j + 1) if j + 1 < n else float('inf')
            down = dfs(i + 1, j) if i + 1 < m else float('inf')

            # Store the result in memo
            memo[(i, j)] = grid[i][j] + min(right, down)
            return memo[(i, j)]

        return dfs(0, 0)

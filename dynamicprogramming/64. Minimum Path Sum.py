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

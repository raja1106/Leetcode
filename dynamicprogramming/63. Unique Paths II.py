from typing import List


class Solution_Bottom_up:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            if obstacleGrid[row][0] == 1:
                break
            dp[row][0] = 1

        for col in range(cols):
            if obstacleGrid[0][col] == 1:
                break
            dp[0][col] = 1

        for row in range(1, rows):
            for col in range(1, cols):
                if obstacleGrid[row][col] == 0:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
                else:
                    dp[row][col] = 0

        return dp[-1][-1]
class Solution_DFS:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def dfs(i, j):
            """
            A depth-first search (DFS) recursive function to compute the number of unique paths
            from the current position (i, j) to the bottom-right corner (m-1, n-1), using memoization
            to store previously computed results.

            Parameters:
            i (int): Current row index in the grid.
            j (int): Current column index in the grid.

            Returns:
            int: The number of unique paths from (i, j) to (m-1, n-1).
            """
            # Base Case 1: If we reach the bottom-right corner, count it as a valid path
            if i == m - 1 and j == n - 1:
                return 1

            # Base Case 2: If we move out of bounds, return 0 (invalid path)
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0

            # Check if the result is already computed (memoization)
            if (i, j) in memo:
                return memo[(i, j)]

            # Recursive calls: Move right (j+1) and move down (i+1)
            memo[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)

            return memo[(i, j)]
        return dfs(0,0)
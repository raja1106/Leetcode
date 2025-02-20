class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0] * n for _ in range(m)]
        for i in range(0,m):
            dp[i][0]=1
        for j in range(0,n):
            dp[0][j]=1

        for row in range(1,m):
            for col in range(1,n):
                dp[row][col]=dp[row-1][col]+dp[row][col-1]
        return dp[-1][-1]

class Solution_Space_Optimized:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n  # Initialize a 1D array with size `n`

        for row in range(1, m):
            for col in range(1, n):
                dp[col] += dp[col - 1]

        return dp[-1]


class Solution_BruteForce_1:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(i, j):
            """
            A depth-first search (DFS) recursive function to compute the number of unique paths
            from cell (i, j) to the top-left corner (0,0), with memoization to avoid redundant calculations.

            Parameters:
            i (int): Row index of the current cell.
            j (int): Column index of the current cell.

            Returns:
            int: The number of unique paths from (i, j) to (0, 0).
            """
            # Base Case 1: If out of bounds, return 0 (invalid path)
            if i < 0 or j < 0:
                return 0

            # Base Case 2: If we reach the top-left corner, count it as a valid path
            if i == 0 and j == 0:
                return 1

            # Check if the result is already computed (memoization)
            if (i, j) in memo:
                return memo[(i, j)]

            # Recursive calls: Move left (j-1) and up (i-1)
            memo[(i, j)] = dfs(i, j - 1) + dfs(i - 1, j)

            return memo[(i, j)]

        return dfs(m - 1, n - 1)


class Solution_Bruteforce_2:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

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
            if i >= m or j >= n:
                return 0

            # Check if the result is already computed (memoization)
            if (i, j) in memo:
                return memo[(i, j)]

            # Recursive calls: Move right (j+1) and move down (i+1)
            memo[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)

            return memo[(i, j)]
        return dfs(0,0)

# Test Cases
sol = Solution()
print(sol.uniquePaths(3, 7))  # Output: 28
print(sol.uniquePaths(3, 2))  # Output: 3
print(sol.uniquePaths(7, 3))  # Output: 28

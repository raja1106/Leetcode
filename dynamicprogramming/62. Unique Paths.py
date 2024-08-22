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

from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        dp[0] = matrix[0]

        for i in range(1,m):
            for j in range(0,n):
                minSumAbove=dp[i-1][j]
                if(j-1>=0):
                  minSumAbove=min(minSumAbove,dp[i-1][j-1])
                if(j+1<n):
                  minSumAbove = min(minSumAbove, dp[i - 1][j+1])
                dp[i][j]=minSumAbove+matrix[i][j]

        return min(dp[n-1])
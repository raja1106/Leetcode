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

        return min(dp[m-1])


class Solution_DFS:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = {}

        def dfs(row, col):
            if col < 0 or col >= n:
                return float('inf')
            if (row, col) in memo:
                return memo[(row, col)]
            if row == len(matrix):
                return 0

            left_sum = right_sum = down_sum = float('inf')
            if col - 1 >= 0:
                left_sum = dfs(row + 1, col - 1)
            if col + 1 < len(matrix):
                right_sum = dfs(row + 1, col + 1)
            down_sum = dfs(row + 1, col)
            memo[(row, col)] = min(left_sum, right_sum, down_sum) + matrix[row][col]
            return memo[(row, col)]

        min_path_sum = float('inf')
        for col in range(len(matrix[0])):
            local_path_sum = dfs(0, col)
            min_path_sum = min(local_path_sum, min_path_sum)

        return min_path_sum



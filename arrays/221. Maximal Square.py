from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        max_side = 0

        for col in range(n):
            if matrix[0][col] == '1':
                dp[0][col] = 1
                max_side = 1

        for row in range(m):
            if matrix[row][0] == '1':
                dp[row][0] = 1
                max_side = 1

        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == '0':
                    dp[row][col] = 0
                else:
                    dp[row][col] = 1 + (
                        min(dp[row][col - 1], dp[row - 1][col], dp[row - 1][col - 1]))
                max_side = max(max_side, dp[row][col])

        return max_side * max_side





class Solution_bruteforce:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dfs(i,j,s1,s2):
            #Base Case
            if i == len(s1) or j == len(s2):
                return 0
            option1 = option2 = option3 =0
            if s1[i] == s2[j]:
                option1 = 1+dfs(i+1,j+1,s1,s2)
            else:
                option2 = dfs(i,j+1,s1,s2)
                option3 = dfs(i+1,j,s1,s2)
            return max(option1,option2,option3)
        return dfs(0,0,text1,text2)


class Solution_Top_Down:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(i,j):
            key = (i,j)
            if key in memo:
                return memo[key]
            if i == len(text1) or j == len(text2):
                return 0
            option1 = option2 = option3 = 0
            if text1[i] == text2[j]:
                option1 = 1+ dfs(i+1,j+1)
            else:
                option2 = dfs(i+1,j)
                option3 = dfs(i,j+1)
            memo[key] = max(option1,option2,option3)
            return memo[key]
        return dfs(0,0)

class Solution_DP_Using_Bottom_Up:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]


class Solution_DP_Using_Bottom_Up_Space_Optimized:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(prev[j], curr[j + 1])
            prev, curr = curr, prev

        return prev[0]
""" ---------------------------------------------------------------------"""


class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:

        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    # If characters match, increment LCS length by 1
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # If characters don't match, take the maximum value from top or left cell
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(s1)][len(s2)]


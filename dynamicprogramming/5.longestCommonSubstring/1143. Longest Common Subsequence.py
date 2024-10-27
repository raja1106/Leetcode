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


class Solution_Top_down:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def findLCSLengthRecursive(s1, s2, i1, i2, count):
            if i1 == len(s1) or i2 == len(s2):
                return count

            # Memoization key should include count
            if (i1, i2, count) in memo:
                return memo[(i1, i2, count)]

            c1 = count

            if s1[i1] == s2[i2]:
                c1 = findLCSLengthRecursive(s1, s2, i1 + 1, i2 + 1, count + 1)

            # Call the recursive function without incrementing the count to explore other paths
            c2 = findLCSLengthRecursive(s1, s2, i1, i2 + 1, count)#count will not reset to zero in subsequence problem
            c3 = findLCSLengthRecursive(s1, s2, i1 + 1, i2, count)

            # Memoize the maximum value
            memo[(i1, i2, count)] = max(c1, c2, c3)
            return memo[(i1, i2, count)]

        return findLCSLengthRecursive(text1, text2, 0, 0, 0)


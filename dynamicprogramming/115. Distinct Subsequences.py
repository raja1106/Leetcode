class Solution_Topdown:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def backtrack(i, j):
            # If t is fully matched, we found a valid subsequence
            if j == len(t):
                return 1
            # If s is exhausted before t is matched
            if i == len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            # Case 1: Match found, two choices - use it or skip it
            if s[i] == t[j]:
                memo[(i, j)] = backtrack(i + 1, j + 1) + backtrack(i + 1, j)
            else:
                # Case 2: No match, skip character in s
                memo[(i, j)] = backtrack(i + 1, j)
            return memo[(i, j)]

        return backtrack(0, 0)


class Solution_Bottom_UP1:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # DP table where dp[i][j] represents numDistinct(s[i:], t[j:])
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case: If t is empty, there is exactly one way (delete all characters)
        for i in range(m + 1):
            dp[i][n] = 1  # When j == len(t), return 1

        # Fill the DP table in bottom-up manner
        for i in range(m - 1, -1, -1):  # Iterate from bottom to top
            for j in range(n - 1, -1, -1):  # Iterate from right to left
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]

        return dp[0][0]  # Return the result from the top-left corner


class Solution_BottomUP2:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # Create DP table initialized to 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case: If t is empty, there is exactly one way to form it
        for i in range(m + 1):
            dp[i][0] = 1  # If t is empty, we can always remove all characters

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:  # If characters match
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:  # If characters do not match
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]


# Test cases
sol = Solution()
print(sol.numDistinct("rabbbit", "rabbit"))  # Output: 3
print(sol.numDistinct("babgbag", "bag"))  # Output: 5

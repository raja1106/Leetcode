class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        memo = {}

        def dfs(i, j, s1, s2):
            # Base Case: If one string is exhausted, append the remaining of the other
            if i == len(s1):
                return s2[j:]
            if j == len(s2):
                return s1[i:]
            if (i, j) in memo:
                return memo[(i, j)]

            # If characters match, include the character and move both pointers
            if s1[i] == s2[j]:
                memo[(i, j)] = s1[i] + dfs(i + 1, j + 1, s1, s2)
                return s1[i] + dfs(i + 1, j + 1, s1, s2)

            # Try both possibilities (either taking s1[i] or s2[j]) and return the shorter one
            option1 = s1[i] + dfs(i + 1, j, s1, s2)  # Include s1[i] and move forward in s1
            option2 = s2[j] + dfs(i, j + 1, s1, s2)  # Include s2[j] and move forward in s2
            memo[(i, j)] = option1 if len(option1) < len(option2) else option2
            return option1 if len(option1) < len(option2) else option2  # Return the shortest

        return dfs(0, 0, str1, str2)

class Solution_Bottom_UP_DP:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Step 1: Compute LCS using Bottom-Up DP
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Step 2: Construct SCS from the dp table by backtracking
        i, j = m, n
        scs = []

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:  # If characters match, take it in SCS
                scs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:  # Move up (take from str1)
                scs.append(str1[i - 1])
                i -= 1
            else:  # Move left (take from str2)
                scs.append(str2[j - 1])
                j -= 1

        # Add remaining characters from str1 or str2
        while i > 0:
            scs.append(str1[i - 1])
            i -= 1
        while j > 0:
            scs.append(str2[j - 1])
            j -= 1

        # Reverse since we built it backwards
        return "".join(reversed(scs))


# Test cases
sol = Solution()
print(sol.shortestCommonSupersequence("abac", "cab"))  # Expected Output: "cabac"
print(sol.shortestCommonSupersequence("geek", "eke"))  # Expected Output: "geeke"

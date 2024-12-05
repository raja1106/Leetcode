class Solution_BruteForce: #2^n
    def findSPMCount(self, str, pat):
        # Variable to store the total count of matching subsequences
        total_count = 0

        # Recursive DFS function to explore all subsequences
        def dfs(i, string, pat, j):
            nonlocal total_count  # Access the outer variable to update the count

            # Base case: If we have matched the entire pattern
            if j == len(pat):
                total_count += 1  # Increment the count for a successful match
                return

            # Base case: If we have reached the end of the string
            if i == len(string):
                return

            # Recursive call: Exclude the current character of the string
            dfs(i + 1, string, pat, j)

            # Recursive call: Include the current character if it matches the pattern
            if string[i] == pat[j]:
                dfs(i + 1, string, pat, j + 1)

            return  # Explicit return for clarity

        # Initiate the DFS traversal starting from index 0 for both string and pattern
        dfs(0, str, pat, 0)

        # Return the total count of matching subsequences
        return total_count
class Solution_Top_Down_Memo: # O(m*n)
    def findSPMCount(self, str, pat):
        # Using a dictionary to store computed results for memoization
        memo = {}

        def dfs(i, string, pat, j):
            # Create a unique key for the current state
            state = (i, j)

            # Return the cached result if it exists
            if state in memo:
                return memo[state]

            # Base case: If the pattern is fully matched, return 1
            if j == len(pat):
                memo[state] = 1
                return 1

            # Base case: If the string is fully traversed without matching the pattern
            if i == len(string):
                memo[state] = 0
                return 0

            # Recursive case: Explore both exclude and include options
            # Option 1: Exclude the current character
            exclude_count = dfs(i + 1, string, pat, j)

            # Option 2: Include the current character if it matches the pattern
            include_count = 0
            if string[i] == pat[j]:
                include_count = dfs(i + 1, string, pat, j + 1)

            # Store the total count in memo and return
            memo[state] = exclude_count + include_count
            return memo[state]

        # Initiate the recursive process
        return dfs(0, str, pat, 0)


class Solution_Bottom_up: #T(n) = O(m*n)
    def findSPMCount(self, str, pat):
        n, m = len(str), len(pat)

        # Initialize a DP table with size (n+1) x (m+1)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Base case: dp[i][0] = 1 for all i (empty pattern)
        for i in range(n + 1):
            dp[i][0] = 1

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # Exclude the current character
                dp[i][j] = dp[i - 1][j]

                # Include the current character if it matches
                if str[i - 1] == pat[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        # The answer is in dp[n][m]
        return dp[n][m]

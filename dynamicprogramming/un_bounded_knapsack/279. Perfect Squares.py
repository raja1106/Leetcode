class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: no squares needed to form 0

        # Iterate over all numbers from 1 to n
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], 1 + dp[i - j * j])
                j += 1

        return dp[n]

class Solution_Using_Memo:
    def numSquares(self, n: int) -> int:
        memo = {}  # Memoization dictionary

        def dfs(i, current_sum):  # Min number of perfect squares needed
            if current_sum == n:
                return 0  # No more numbers needed
            if current_sum > n or i * i > n:
                return float('inf')  # Invalid case (impossible sum)
            if (i, current_sum) in memo:
                return memo[(i, current_sum)]  # Return cached result

            # Exclude current perfect square (move to next square)
            exclude_current = dfs(i + 1, current_sum)
            # Include current perfect square (use it again)
            include_current = dfs(i, current_sum + i * i) + 1

            memo[(i, current_sum)] = min(exclude_current, include_current)
            return memo[(i, current_sum)]

        result = dfs(1, 0)
        return result if result != float('inf') else -1

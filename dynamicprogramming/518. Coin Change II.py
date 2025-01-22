class Solution_Bruteforce_Way:
    def change(self, amount: int, coins: List[int]) -> int:
        total_count = 0

        def dfs(i, current_amount):
            nonlocal total_count
            if current_amount == amount:
                total_count += 1
                return
            if current_amount > amount or i == len(coins):
                return

            # Exclude current coin
            dfs(i + 1, current_amount)
            # Include current coin (take it again)
            dfs(i, current_amount + coins[i])

        dfs(0, 0)
        return total_count


class Solution_TopDown_Memo:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}  # Memoization dictionary

        def dfs(i, current_amount):  # How many ways you can form amount from index 'i'
            if current_amount == amount:
                return 1  # Found one valid way
            if current_amount > amount or i == len(coins):
                return 0  # No valid solution

            # If result is already computed, return it
            if (i, current_amount) in memo:
                return memo[(i, current_amount)]

            # Exclude current coin
            exclude_current = dfs(i + 1, current_amount)
            # Include current coin (take it again)
            include_current = dfs(i, current_amount + coins[i])

            memo[(i, current_amount)] = exclude_current + include_current
            return memo[(i, current_amount)]

        return dfs(0, 0)


from typing import List


class Solution_Using_2D_DP:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # Base Case: One way to make amount 0 (by taking nothing)
        for i in range(n + 1):
            dp[i][0] = 1

        # Fill DP Table
        for i in range(1, n + 1):  # Iterate over coins
            for j in range(amount + 1):  # Iterate over possible amounts
                dp[i][j] = dp[i - 1][j]  # Exclude current coin
                if j - coins[i - 1] >= 0:  # Include current coin
                    dp[i][j] += dp[i][j - coins[i - 1]]

        return dp[n][amount]

class Solution_1D_DP_Array:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # Base case: one way to make amount 0 (by taking nothing)

        for coin in coins:  # Iterate over coins first
            for i in range(coin, amount + 1):  # Then iterate over possible amounts
                dp[i] += dp[i - coin]

        return dp[amount]
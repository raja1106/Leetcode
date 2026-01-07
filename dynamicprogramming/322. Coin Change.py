from typing import List

class Solution_Topdown_withBetter_Space_Complexity:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}  # Memoization dictionary

        def dfs(current_amount): # min number of coins needed
            if current_amount == amount:
                return 0  # No more coins needed
            if current_amount > amount:
                return float('inf')  # Invalid case (impossible amount)
            if current_amount in memo:
                return memo[current_amount]  # Return cached result

            min_coins = float('inf')

            for coin in coins:
                min_coins = min(min_coins, 1+ dfs(current_amount+coin))


            memo[current_amount] = min_coins
            return memo[current_amount]

        result = dfs(0)
        return result if result != float('inf') else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            min_coins = float('inf')
            for coin in coins:
                if coin <= i:
                    min_coins = min(min_coins, 1 + dp[i - coin])
            dp[i] = min_coins
        return dp[amount] if dp[amount] != float('inf') else -1

class Solution_Bruteforce:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(i, remaining_amount):
            if remaining_amount == 0:
                return 0  # No more coins needed
            if remaining_amount < 0 or i == len(coins):
                return float('inf')  # Invalid case (unreachable amount)

            # Exclude current coin
            exclude_current = dfs(i + 1, remaining_amount)
            # Include current coin (take it again)
            include_current = dfs(i, remaining_amount - coins[i]) + 1

            return min(exclude_current, include_current)

        result = dfs(0, amount)
        return result if result != float('inf') else -1


from typing import List


class Solution_Top_Down_Memo:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}  # Memoization dictionary

        def dfs(i, current_amount): # min number of coins needed
            if current_amount == amount:
                return 0  # No more coins needed
            if current_amount > amount or i == len(coins):
                return float('inf')  # Invalid case (impossible amount)
            if (i, current_amount) in memo:
                return memo[(i, current_amount)]  # Return cached result

            # Exclude current coin
            exclude_current = dfs(i + 1, current_amount)
            # Include current coin (take it again)
            include_current = dfs(i, current_amount + coins[i]) + 1

            memo[(i, current_amount)] = min(exclude_current, include_current)
            return memo[(i, current_amount)]

        result = dfs(0, 0)
        return result if result != float('inf') else -1


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
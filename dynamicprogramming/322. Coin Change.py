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


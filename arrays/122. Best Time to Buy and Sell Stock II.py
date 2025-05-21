from typing import List


class Solution_Greedy:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        total_profit = 0

        for i in range(1, n):  # Start from day 1
            if prices[i] > prices[i - 1]:  # If today's price is higher, add profit
                total_profit += prices[i] - prices[i - 1]

        return total_profit

class Solution_Bottom_Up:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp[i][ready_to_buy] where ready_to_buy ∈ {0, 1}
        dp = [[0] * 2 for _ in range(n + 1)]

        # Fill from day n-1 down to 0
        for i in range(n - 1, -1, -1):
            for ready_to_buy in [0, 1]:
                if ready_to_buy:
                    buy_today = -prices[i] + dp[i + 1][0]
                    skip_buy = dp[i + 1][1]
                    dp[i][1] = max(buy_today, skip_buy)
                else:
                    sell_today = prices[i] + dp[i + 1][1]
                    skip_sell = dp[i + 1][0]
                    dp[i][0] = max(sell_today, skip_sell)

        # Start at day 0, ready to buy
        return dp[0][1]

class Solution_Top_Down:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i: int, can_buy: bool) -> int:
            if i == len(prices):
                return 0

            if (i, can_buy) in memo:
                return memo[(i, can_buy)]

            max_profit = 0

            if can_buy:
                # Option 1: Buy the stock today
                buy_today = -prices[i] + dfs(i + 1, False)
                # Option 2: Skip buying today
                skip_buy = dfs(i + 1, True)
                max_profit = max(buy_today, skip_buy)
            else:
                # Option 1: Sell the stock today
                sell_today = prices[i] + dfs(i + 1, True)
                # Option 2: Skip selling today
                skip_sell = dfs(i + 1, False)
                max_profit = max(sell_today, skip_sell)

            memo[(i, can_buy)] = max_profit
            return max_profit

        return dfs(0, True)

class Solution_Bottom_UP_Constant:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # Only need to keep track of next day's results: [not ready_to_buy, ready_to_buy]
        next_day = [0, 0]  # dp[i + 1][0] and dp[i + 1][1]

        for i in range(n - 1, -1, -1):
            current_day = [0, 0]
            for ready_to_buy in [0, 1]:
                if ready_to_buy:
                    buy_today = -prices[i] + next_day[0]
                    skip_buy = next_day[1]
                    current_day[1] = max(buy_today, skip_buy)
                else:
                    sell_today = prices[i] + next_day[1]
                    skip_sell = next_day[0]
                    current_day[0] = max(sell_today, skip_sell)
            next_day = current_day

        return next_day[1]

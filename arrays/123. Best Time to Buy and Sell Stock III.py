from typing import List

class Solution_Bottom_Up:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[i][can_buy][transaction_count] = max profit from day i
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for can_buy in [0, 1]:
                for transaction_count in range(3):  # 0, 1, 2 (but 2 is max so no buy if t==2)
                    profit = 0
                    if can_buy and transaction_count < 2:
                        buy_option = -prices[i] + dp[i + 1][0][transaction_count + 1]
                        not_buy_option = dp[i + 1][1][transaction_count]
                        profit = max(buy_option, not_buy_option)
                    elif not can_buy:
                        sell_option = prices[i] + dp[i + 1][1][transaction_count]
                        not_sell_option = dp[i + 1][0][transaction_count]
                        profit = max(sell_option, not_sell_option)
                    dp[i][can_buy][transaction_count] = profit

        return dp[0][1][0]  # Start from day 0, allowed to buy, 0 transactions done
class Solution_Top_Down:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i,can_buy,transaction_count):
            if i == len(prices):
                return 0
            if (i,can_buy,transaction_count) in memo:
                return memo[(i,can_buy,transaction_count)]
            profit = 0
            if can_buy and transaction_count < 2:
                buy_option = -prices[i] + dfs(i+1,False,transaction_count+1)
                not_buy_option = dfs(i+1,True,transaction_count)
                profit = max(buy_option,not_buy_option)
            elif not can_buy:#sell area
                sell_option = prices[i] + dfs(i+1,True,transaction_count)
                not_sell_option = dfs(i+1,False,transaction_count)
                profit = max(sell_option,not_sell_option)
            memo[(i,can_buy,transaction_count)] = profit
            return profit
        return dfs(0,True,0)


class Solution_Constant_space:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # Initialize next_day and current as 2 x 3 DP tables
        next_day = [[0] * 3 for _ in range(2)]

        for i in range(n - 1, -1, -1):
            current = [[0] * 3 for _ in range(2)]
            for can_buy in [0, 1]:
                for transaction_count in range(3):
                    if can_buy and transaction_count < 2:
                        buy_option = -prices[i] + next_day[0][transaction_count + 1]
                        skip_buy = next_day[1][transaction_count]
                        current[1][transaction_count] = max(buy_option, skip_buy)
                    elif not can_buy:
                        sell_option = prices[i] + next_day[1][transaction_count]
                        skip_sell = next_day[0][transaction_count]
                        current[0][transaction_count] = max(sell_option, skip_sell)
            next_day = current

        return next_day[1][0]  # Start at day 0, can_buy = 1, transaction_count = 0

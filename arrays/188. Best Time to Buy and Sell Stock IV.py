from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k == 0 or n == 0:
            return 0

        # If k >= n/2, it's unlimited transactions case
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                profit += max(prices[i] - prices[i - 1], 0)
            return profit

        # next_day[can_buy][transaction_count] where transaction_count ∈ [0, k]
        next_day = [[0] * (k + 1) for _ in range(2)]

        for i in range(n - 1, -1, -1):
            current_day = [[0] * (k + 1) for _ in range(2)]
            for can_buy in [0, 1]:
                for t in range(k + 1):
                    if can_buy and t < k:
                        buy_today = -prices[i] + next_day[0][t + 1]
                        skip_buy = next_day[1][t]
                        current_day[1][t] = max(buy_today, skip_buy)
                    elif not can_buy:
                        sell_today = prices[i] + next_day[1][t]
                        skip_sell = next_day[0][t]
                        current_day[0][t] = max(sell_today, skip_sell)
            next_day = current_day

        return next_day[1][0]
class Solution_Top_Down:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        memo = {}
        def dfs(i,can_buy,transaction_count):
            if i == len(prices):
                return 0
            if (i,can_buy,transaction_count) in memo:
                return memo[(i,can_buy,transaction_count)]
            profit = 0
            if can_buy and transaction_count < k:
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
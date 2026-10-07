from typing import List

#[7,1,5,3,6,4]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        local_profit=0
        lowest_sofar=prices[0]

        for i in range(1,len(prices)):
            local_profit=prices[i]-lowest_sofar
            max_profit=max(max_profit,local_profit)
            lowest_sofar=min(lowest_sofar,prices[i])
        return max_profit

"""
Input: prices = [7,1,5,3,6,4]
smallest_so_far
            x
        y
    z
"""
class Solution_DP1:
    def maxProfit(self, prices: list[int]) -> int:
        memo = {}
        def dfs(i,can_buy):
            if (i,can_buy) in memo:
                return memo[(i,can_buy)]
            if i == len(prices):
                return 0
            if can_buy:
                skip_buy = dfs(i+1,can_buy)
                buy_today = dfs(i+1,False)-prices[i]
                memo[(i,can_buy)] = max(skip_buy,buy_today)
                return max(skip_buy,buy_today)
            else:
                skip_sell = dfs(i+1,can_buy)
                sell_today = prices[i]
                memo[(i,can_buy)] = max(skip_sell,sell_today)
                return max(skip_sell,sell_today)

        return dfs(0,True)

class Solution_DP:
    def maxProfit(self, prices: List[int]) -> int:
        """
        prices = [7,1,5,3,6,4]

        buy today or skip today

        if you already bought it, then the only option you have is selling, when seliing is the
        only option, sell it or skip it

        if Buy:
            buy today or skip,
            you are losing money while buying it

        if Sell:
            sell today or skip today
            you are gaining money while selling it
        """
        memo = {}

        def dfs(i, is_buy, purchase_count):
            if (i, is_buy, purchase_count) in memo:
                return memo[(i, is_buy, purchase_count)]
            if i == len(prices):
                return 0

            if is_buy:
                buy_today = -prices[i] + dfs(i + 1, False, purchase_count - 1)
                skip_buy_today = dfs(i + 1, True, purchase_count)
                memo[(i, is_buy, purchase_count)] = max(buy_today, skip_buy_today)
                return max(buy_today, skip_buy_today)
            else:
                if purchase_count <= 0:
                    sell_today = prices[i]
                else:
                    sell_today = prices[i] + dfs(i + 1, True, purchase_count)
                skip_sell_today = dfs(i + 1, False, purchase_count)
                memo[(i, is_buy, purchase_count)] = max(sell_today, skip_sell_today)
                return max(sell_today, skip_sell_today)

        return dfs(0, True, 1)






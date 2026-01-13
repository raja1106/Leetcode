class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i,can_buy):
            if i >= len(prices):
                return 0
            if (i,can_buy) in memo:
                return memo[(i,can_buy)]
            profit = 0
            if can_buy:
                buy_option = -prices[i] + dfs(i+1,False)
                not_buy_option = dfs(i+1,True)
                profit = max(buy_option,not_buy_option)
            else:#sell area
                sell_option = prices[i] + dfs(i+2,True)
                not_sell_option = dfs(i+1,False)
                profit = max(sell_option,not_sell_option)
            memo[(i,can_buy)] = profit
            return profit
        return dfs(0,True)
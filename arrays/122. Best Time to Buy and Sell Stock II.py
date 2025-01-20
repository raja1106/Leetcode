from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        total_profit = 0

        for i in range(1, n):  # Start from day 1
            if prices[i] > prices[i - 1]:  # If today's price is higher, add profit
                total_profit += prices[i] - prices[i - 1]

        return total_profit


class Solution_1:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_so_far = prices[0]
        total_profit = 0
        for i in range(n):
            if prices[i] > min_so_far:
                total_profit += prices[i] - min_so_far
            min_so_far = prices[i]

        return total_profit
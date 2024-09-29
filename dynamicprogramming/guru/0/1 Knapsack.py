'''
Given two integer arrays to represent weights and profits of 'N' items, we need to
find a subset of these items which will give us maximum profit such that their
cumulative weight is not more than a given number 'C'.
Write a function that returns the maximum profit. Each item can only be selected once, which means either we put an item in the knapsack or skip it.

'''

class Solution_Bruteforce:
  def solveKnapsack(self, profits, weights, capacity):
    max_profit = 0
    def subset(i,slate,current_profit):
      nonlocal max_profit
      if sum(slate) > capacity:#Back tracking
        return
      if i == len(profits):
        max_profit = max(max_profit,current_profit)
        return
    # exclude
      subset(i+1,slate,current_profit)
    # include
      slate.append(weights[i])
      subset(i+1,slate,current_profit+profits[i])
      slate.pop()
    subset(0,[],0)
    return max_profit
class Solution:
    def solveKnapsack(self, profits, weights, capacity):
        n = len(weights)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        for current_weight in range(capacity + 1):
            dp[0][current_weight] = 0
        for i in range(1, n + 1):
            for weight in range(capacity + 1):
                if weight - weights[i - 1] >= 0:
                    dp[i][weight] = max(dp[i - 1][weight], dp[i - 1][weight - weights[i - 1]] + profits[i - 1])
                else:
                    dp[i][weight] = dp[i - 1][weight]

        return dp[n][capacity]
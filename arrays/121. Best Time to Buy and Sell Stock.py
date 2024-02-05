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
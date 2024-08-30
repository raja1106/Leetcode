from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*len(cost)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range (2,len(cost)):
            dp[i]=min(dp[i-1],dp[i-2])+cost[i]
        return min(dp[-1],dp[-2])


class Solution_1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        dp = [0] * len(cost)

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return dp[-1]



class Solution_2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Computes the minimum cost to reach the top of the staircase.

        Parameters:
        - cost (List[int]): List of integers where each element represents the cost at each step.

        Returns:
        - int: Minimum cost to reach the top of the staircase.
        """
        # Edge case: if the list is too small, the result is simply the minimum of the costs.
        if len(cost) <= 2:
            return min(cost)

        # Variables to store the minimum cost to reach the previous two steps.
        two_steps_back = cost[0]
        one_step_back = cost[1]

        # Iterate from step 2 to the end of the cost list.
        for i in range(2, len(cost)):
            current = min(one_step_back, two_steps_back) + cost[i]
            two_steps_back = one_step_back
            one_step_back = current

        # The answer is the minimum cost to reach the last or the second-last step.
        return min(one_step_back, two_steps_back)


# Example usage
sol = Solution()
print(sol.minCostClimbingStairs([10, 15, 20]))  # Expected output: 15
print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # Expected output: 6



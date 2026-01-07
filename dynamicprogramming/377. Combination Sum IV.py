from typing import List

class Solution_Top_Down_Way_Latest:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}  # Memoization dictionary

        def dfs(current_amount): # min number of coins needed
            if current_amount == target:
                return 1  # valid path found
            if current_amount > target:
                return 0  # no valid path available
            if current_amount in memo:
                return memo[current_amount]  # Return cached result

            current_total = 0

            for coin in nums:
                current_total = current_total + dfs(current_amount+coin)

            memo[current_amount] = current_total
            return memo[current_amount]

        result = dfs(0)
        return result

class Solution_Top_Down_Way:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(current_sum):
            if current_sum == target:
                return 1 # One valid combination
            if current_sum > target:
                return 0
            if current_sum in memo:
                return memo[current_sum]
            total = 0
            for num in nums:
                total += dfs(current_sum + num)
            memo[current_sum] = total
            return total

        return dfs(0)


class Solution_TopDown_way_Wrong: # Because this is subset approach. Not permutation approach
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(current_sum, i):
            if current_sum == target:
                return 1
            elif current_sum > target or len(nums) == i:
                return 0
            if (current_sum, i) in memo:
                return memo[(current_sum, i)]
            exclude_current = dfs(current_sum, i + 1)
            include_current = dfs(current_sum + nums[i], i)
            memo[(current_sum, i)] = include_current + exclude_current
            return memo[(current_sum, i)]

        return dfs(0, 0)


class Solution_Bottom_Up_Approach:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1  # Base case: one way to reach target sum 0

        # Build the DP table where dp[i] represents the number of ways to get sum i
        for i in range(1, target + 1):
            for num in nums:
                if i-num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        def dfs(i,sum):
            nonlocal count
            if i == len(nums):
                if sum == target:
                    count += 1
                return
            dfs(i+1,sum+nums[i])
            dfs(i+1,sum-nums[i])
        dfs(0,0)
        return count

class Solution_BetterBruteForceway:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i,sum):
            if i == len(nums):
                if sum == target:
                    return 1
                else:
                    return 0
            add = dfs(i+1,sum+nums[i])
            subtract = dfs(i+1,sum-nums[i])
            return add+subtract
        return dfs(0,0)


class Solution_UsingMemo_Approach:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}  # Dictionary to store the result of subproblems

        def dfs(i, current_sum):
            memo_key = (i, current_sum)
            # If the result of this state has already been computed, return it
            if memo_key in memo:
                return memo[memo_key]

            # Base case: If we've gone through all numbers
            if i == len(nums):
                return 1 if current_sum == target else 0

            # Recurse by choosing both adding and subtracting the current number
            add = dfs(i + 1, current_sum + nums[i])
            subtract = dfs(i + 1, current_sum - nums[i])

            # Store the result in memo before returning it
            memo[memo_key] = add + subtract
            return memo[memo_key]

        # Start the recursion from index 0 and initial sum 0
        return dfs(0, 0)


class Solution_Using_DP:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)

        # If (totalSum + target) is odd or target is out of bounds, return 0
        if (totalSum + target) % 2 != 0 or totalSum < abs(target):
            return 0

        subsetSum = (totalSum + target) // 2

        # Initialize DP table
        dp = [[0] * (subsetSum + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 1  # Base case: one way to make sum 0 (by selecting nothing)

        # First column should be initialized to 1 (one way to make sum 0)
        for i in range(len(nums) + 1):
            dp[i][0] = 1

        # Fill the DP table
        for i in range(1, len(nums) + 1):
            for j in range(subsetSum + 1):
                dp[i][j] = dp[i - 1][j]  # Exclude current number
                if j - nums[i - 1] >= 0:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]  # Include current number

        return dp[len(nums)][subsetSum]

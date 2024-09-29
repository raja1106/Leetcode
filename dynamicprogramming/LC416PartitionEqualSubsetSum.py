from typing import List

"""
Let's try to populate our dp[][] array from the above solution, working in a bottom-up fashion. Essentially, we want to find if we can make all possible sums with every subset. This means, dp[i][s] will be 'true' if we can make sum 's' from the first 'i' numbers.
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        targetSum,remainder = divmod(sum(nums),2)
        if remainder:
            return False
        dp = [[False] * (targetSum+1) for _ in range(len(nums)+1)]
        dp[0][0]=True
        #making 1st columns as true
        for i in range (0,len(nums)+1):
            dp[i][0]=True

        for i in range(1,len(nums)+1):
            for j in range(1,targetSum+1):
                dp[i][j] = dp[i-1][j]
                if(j-nums[i-1]>=0):
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]

        return dp[len(nums)][targetSum]


class Solution_Bruteforce:
    def canPartition(self, nums: List[int]) -> bool:
        partition_sum, remain = divmod(sum(nums), 2)
        if remain == 1:
            return False

        def dfs(i, current_sum):
            if current_sum > partition_sum:
                return False
            if i == len(nums):
                if current_sum == partition_sum:
                    return True
                else:
                    return False
            # exclude
            is_left_true = dfs(i + 1, current_sum)
            # include
            is_right_true = dfs(i + 1, current_sum + nums[i])

            return is_left_true or is_right_true

        return dfs(0, 0)


class Solution_Using_Memozation:
    def canPartition(self, nums: List[int]) -> bool:
        partition_sum, remain = divmod(sum(nums), 2)
        if remain == 1:
            return False
        memo = {}

        def dfs(i, current_sum):
            memo_key = (i, current_sum)
            if memo_key in memo:
                return memo[memo_key]
            if current_sum > partition_sum:
                return False
            if i == len(nums):
                if current_sum == partition_sum:
                    return True
                else:
                    return False
            # exclude
            is_left_true = dfs(i + 1, current_sum)
            # include
            is_right_true = dfs(i + 1, current_sum + nums[i])
            memo[memo_key] = is_left_true or is_right_true
            return is_left_true or is_right_true

        return dfs(0, 0)

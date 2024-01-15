from typing import List


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
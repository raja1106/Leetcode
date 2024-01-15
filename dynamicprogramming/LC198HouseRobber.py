from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp =[0]*len(nums)
        dp[0]=nums[0]

        if(len(nums)>1):
            dp[1]=max(nums[0],nums[1])
        if (len(nums) > 2):
            dp[2] = max(nums[0]+nums[2], nums[1])

        for i in range (3,len(nums)):
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
        return dp[-1]

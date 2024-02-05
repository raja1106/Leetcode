from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=nums[0]
        globalSum=nums[0]
        for i in range(1,len(nums)):
            maxSum = max(maxSum+nums[i],nums[i])
            globalSum=max(maxSum,globalSum)
        return globalSum

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #2,1
        for i in range(len(nums)):
            while(i != nums[i]-1):
                d = nums[i] - 1
                if 0 <= d < len(nums) and nums[i] != nums[d]:
                   nums[i],nums[d]=nums[d],nums[i]
                else:
                   break

        for i in range(len(nums)):
            if(i+1 != nums[i]):
                return i+1

        return len(nums)+1
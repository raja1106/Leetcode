from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count=0
        left=0
        window_product=1
        if nums[0] < k:
            count=1
            window_product=nums[0]
        else:
            window_product =1
            left=1

        for i in range(1,len(nums)):

            window_product *= nums[i]
            while left <= i and window_product >=k:
                window_product = window_product//nums[left]
                left += 1

            count = count+(i-left+1)
        return count
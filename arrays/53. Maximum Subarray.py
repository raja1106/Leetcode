from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = max(current_sum, max_sum)
        return max_sum


class Solution_Using_Prefix_sum:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize prefix sum and min_prefix_sum
        max_sum = nums[0]
        prefix_sum = 0
        min_prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            max_sum = max(max_sum, prefix_sum - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum)

        return max_sum

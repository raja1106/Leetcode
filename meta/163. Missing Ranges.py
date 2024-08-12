from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []

        # Handle case where nums is empty
        if not nums:
            return [[lower, upper]]

        # Check for missing range before the first element
        if nums[0] > lower:
            result.append([lower, nums[0] - 1])

        # Check for missing ranges between consecutive elements
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                result.append([nums[i - 1] + 1, nums[i] - 1])

        # Check for missing range after the last element
        if nums[-1] < upper:
            result.append([nums[-1] + 1, upper])

        return result
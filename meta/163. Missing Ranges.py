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


class Solution1:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        missing_ranges = []
        current_start = lower  # pointer to the current range start

        for num in nums:
            if current_start == num:
                current_start += 1
            else:
                missing_ranges.append([current_start, num - 1])
                current_start = num + 1

        if current_start <= upper:
            missing_ranges.append([current_start, upper])

        return missing_ranges

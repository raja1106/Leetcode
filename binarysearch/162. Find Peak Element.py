from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
        start = 1
        end = len(nums) - 2

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid + 1] > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1


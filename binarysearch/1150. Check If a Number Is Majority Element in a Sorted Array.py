class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        first = self.firstGreaterEqual(nums, target)
        last = self.firstGreaterEqual(nums, target + 1)
        if last-first > len(nums)//2:
            return True
        else:
            return False
    def firstGreaterEqual(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        return start

import bisect
class Solution_Using_Bisect:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # Find first occurrence using binary search
        left_index = bisect.bisect_left(nums, target)
        right_index = bisect.bisect_right(nums, target)
        # Number of times target appears
        count = right_index - left_index #1 2 2 2 3
        # Return True if count is greater than half of the array size
        return count > len(nums) // 2

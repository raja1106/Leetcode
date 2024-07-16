class Solution:
    def searchRange(self, nums, target):
        first = self.firstGreaterEqual(nums, target)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        last = self.firstGreaterEqual(nums, target + 1) - 1
        return [first, last]

    def firstGreaterEqual(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid-1
            else:
                start = mid + 1
        return start

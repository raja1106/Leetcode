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
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[-1]:
                start = mid + 1
            else:
                end = mid - 1

        return nums[start]
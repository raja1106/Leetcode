class Solution:  # [3,4,5,1,2]
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] <= nums[-1]:
                end = mid - 1
            else:
                start = mid + 1

        return nums[start]

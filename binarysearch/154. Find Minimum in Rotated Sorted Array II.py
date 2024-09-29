class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_found = None
        for i in range(len(nums)):
            if nums[i] != nums[-1]:
                left_found = i
                break
        if left_found is None:
            return nums[0]
        start = left_found
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[-1]:
                start = mid+1
            else:
                end = mid-1

        return nums[start]
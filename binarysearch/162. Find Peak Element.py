from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1

        #At this point we know any peak must be in interior

        start=0
        end=len(nums)-1

        while start <=end:
            mid=start+(end-start)//2
            if mid != 0 and mid != len(nums)-1 and nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif mid != 0 and mid != len(nums)-1 and nums[mid-1] > nums[mid] < nums[mid+1]:
                end=mid-1  # or start=mid+1 also works
            elif mid == 0 or nums[mid-1] < nums[mid]:
                start=mid+1
            else:
                end=mid-1

    # this is easy implementation
    def findPeakElement_Neetcode(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (end + start) // 2
            if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                start = mid + 1
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                end = mid - 1
            else:
                return mid


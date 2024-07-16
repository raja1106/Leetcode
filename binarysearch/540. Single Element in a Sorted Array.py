from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        start,end = 0,len(nums)-1
        while(start <=end):
            mid = start+(end-start)//2
            leftSize=mid-start
            rightSize=end-mid
            if mid != 0 and nums[mid] == nums[mid-1]:
                leftSize=leftSize-1
            elif (mid != len(nums)-1) and nums[mid] == nums[mid+1]:
                rightSize =rightSize-1
            else:
                return nums[mid]

            if leftSize%2 != 0:
                end=mid-1
            else:
                start=mid+1

        return -1

    def singleNonDuplicate_Feb11(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        start, end = 0, len(nums) - 1
        while (start <= end):
            mid = start + (end - start) // 2
            if (nums[mid] != nums[mid + 1]) and (nums[mid] != nums[mid - 1]):
                return nums[mid]
            elif (mid % 2 == 0 and nums[mid + 1] == nums[mid]) or (mid % 2 == 1 and nums[mid - 1] == nums[mid]):
                start = mid + 1
            else:
                end = mid - 1


from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def swap(i: int,j: int)->None:
            nums[i],nums[j] = nums[j],nums[i]
        """
        Do not return anything, modify nums in-place instead.
        """
        low =0
        high = len(nums)-1
        mid =0

        while mid <=high:
            if nums[mid] == 0:
                swap(nums,low,mid)
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                swap(nums,mid,high)
                high -=1

        return nums


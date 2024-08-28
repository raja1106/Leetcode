from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while i != nums[i] - 1:
                d = nums[i] - 1
                if nums[d] != nums[i]:
                    nums[d], nums[i] = nums[i], nums[d]
                else:
                    return nums[d]


        return -1


class Solution_gpt:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] - 1 < n and nums[i] != i + 1:
                target_index = nums[i] - 1
                if nums[i] == nums[target_index]:
                    break
                nums[i], nums[target_index] = nums[target_index], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return nums[i]
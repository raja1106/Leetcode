from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        nums_length = len(nums)
        #Re-arrange section
        for i in range(nums_length):
            while i + 1 != nums[i]:
                target_index = nums[i] - 1
                if nums[target_index] != nums[i]:
                    nums[target_index], nums[i] = nums[i], nums[target_index]
                else:
                    break
        #Finding section
        for i in range(nums_length):
            if i + 1 != nums[i]:
                result.append(nums[i])
        return result


class Solution_1:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            while i != nums[i] - 1:
                d = nums[i] - 1
                if nums[d] != nums[i]:
                    nums[d], nums[i] = nums[i], nums[d]
                else:
                    break
        for i in range(len(nums)):
            if(i+1 != nums[i]):
                result.append(nums[i])

        return result
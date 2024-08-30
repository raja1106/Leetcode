from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length):
            while i != nums[i] - 1:
                target_index = nums[i] - 1
                if nums[i] != nums[target_index]:
                    nums[i], nums[target_index] = nums[target_index], nums[i]
                else:
                    break
        #Find
        for i in range(length):
            if i + 1 != nums[i]:
                return [nums[i], i + 1]

        return [-1, -1]
class Solution_1:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            while i != nums[i] - 1:
                d = nums[i] - 1
                if nums[d] != nums[i]:
                    nums[d], nums[i] = nums[i], nums[d]
                else:
                    break
        for i in range(len(nums)):
            if (i + 1 != nums[i]):
                result.append(nums[i])
                result.append(i + 1)

        return result
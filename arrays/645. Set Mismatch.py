from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            while i != nums[i] - 1:
                d = nums[i] - 1
                if nums[d] != nums[i]:
                    nums[d], nums[i] = nums[i], nums[d]
                else:
                    result .append(nums[d])
        for i in range(len(nums)):
            if (i + 1 != nums[i]):
                result.append(i + 1)

        return result
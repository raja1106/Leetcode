from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        nums = [i for i in range(1, 10)]
        self.buildcombinationSum3(0, nums, [], result, k, n)
        return result

    def buildcombinationSum3(self, i, nums, slate, result, k, n):
        if len(slate) >= k or sum(slate) >= n:
            if len(slate) == k and sum(slate) == n:
                result.append(slate[:])
            return

        if i == len(nums):
            return

        # exclusive case
        self.buildcombinationSum3(i + 1, nums, slate, result, k, n)

        # inclusive case
        slate.append(nums[i])
        self.buildcombinationSum3(i + 1, nums, slate, result, k, n)
        slate.pop()
        return








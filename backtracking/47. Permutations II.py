from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()

        if nums is None or len(nums) == 0:
            return ans
        nums.sort()
        self.buildPermutations(0, nums, [], result)
        return list(result)

    def buildPermutations(self, i, nums, current_permutation, result):
        def swap(x, y):
            nums[x], nums[y] = nums[y], nums[x]

        if i == len(nums):
            result.add(tuple(current_permutation[:]))
            return

        for j in range(i, len(nums)):
            current_permutation.append(nums[j])
            swap(j, i)
            self.buildPermutations(i + 1, nums, current_permutation, result)
            current_permutation.pop()
            swap(j, i)
        return
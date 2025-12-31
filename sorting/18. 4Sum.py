class Solution:
    def fourSum(self,nums, target):
        nums.sort()
        result_set = set()
        n = len(nums)

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                left, right = j + 1, n - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        result_set.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return list(result_set)


from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result_set = set()
        n = len(nums)

        for i in range(n - 3):
            # skip duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # skip duplicate j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]

                    if s == target:
                        result_set.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1

                        # skip duplicate left/right after finding a match
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif s < target:
                        left += 1
                    else:
                        right -= 1

        # convert tuples -> lists (LeetCode format)
        return [list(t) for t in sorted(result_set)]
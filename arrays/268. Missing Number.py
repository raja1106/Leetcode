from typing import List


class Solution:
    def missingNumberUsingSorting(self, nums: List[int]) -> int:  # T(n)=O(nlogn)+O(n)
        nums.sort()
        for i in range(len(nums)):
            if (i != nums[i]):
                return i
        return len(nums)

    def missingNumber(self, nums: List[int]) -> int:  # T(n)= O(n)

        for i in range(len(nums)):  # 2,0,1 --> 1,0,2 --> 0,1,2

            while i != nums[i]:
                d = nums[i]
                if d < len(nums):
                    nums[i], nums[d] = nums[d], nums[i]
                else:
                    break

        for i in range(len(nums)):

            if i != nums[i]:
                return i

        return len(nums)


class Solution_Using_Set:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums_set = set(nums)

        for i in range(n + 1):
            if i not in nums_set:
                return i


# Example usage
solution = Solution()
print(solution.missingNumber([3, 0, 1]))  # Expected output: 2

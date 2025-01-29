from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start  # Position to insert `target`

    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []  # Tracks the smallest possible LIS sequence

        for num in nums:
            pos = self.searchInsert(sub, num)  # Find correct position to replace or insert

            if pos == len(sub):
                sub.append(num)  # Extend LIS if num is largest
            else:
                sub[pos] = num  # Replace element to maintain LIS potential

        return len(sub)  # Length of 'sub' is the LIS length


# Test Cases
sol = Solution()
print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Expected Output: 4
print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))  # Expected Output: 4
print(sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # Expected Output: 1
print(sol.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))  # Expected Output: 6

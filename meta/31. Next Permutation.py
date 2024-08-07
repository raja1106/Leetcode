from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the rightmost ascending pair
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:  # If such a pair is found
            # Find the rightmost element that exceeds nums[i]
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap the found element with nums[i]
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the sequence from i+1 to the end
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# Example usage:
nums = [4, 5, 3, 2, 1]
Solution().nextPermutation(nums)
print(nums)  # Output: [5, 1, 2, 3, 4]

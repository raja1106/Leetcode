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
from typing import List

class Solution_previousPermutation:
    def previousPermutation(self, nums: List[int]) -> None:
        """
        Modify nums in-place to produce the previous lexicographical permutation.
        If no such permutation exists (i.e., the array is sorted in ascending order),
        rearrange it to the highest possible order (descending).
        """
        # Find the rightmost index 'i' where nums[i] > nums[i+1].
        # This marks the first element (from the right) that can be swapped to decrease the permutation.
        i = len(nums) - 2
        while i >= 0 and nums[i] <= nums[i + 1]:
            i -= 1

        if i >= 0:  # If such an index is found
            # Find the rightmost element that is less than nums[i].
            j = len(nums) - 1
            while nums[j] >= nums[i]:
                j -= 1
            # Swap nums[i] with nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the sequence from i+1 to the end.
        # This ensures that the suffix is in descending order,
        # which is the largest order, giving the immediate previous permutation.
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# Example usage:
nums = [1, 3, 2]
Solution_previousPermutation().previousPermutation(nums)
print(nums)  # Expected Output: [1, 2, 3] (since [1,3,2] -> [1,2,3] is the immediate previous permutation in lexicographical order)

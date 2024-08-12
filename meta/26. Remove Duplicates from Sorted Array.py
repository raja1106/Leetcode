from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize the first pointer. Pointer i keeps track of the position in the array
        # where the next unique element should be placed.
        i = 0

        # Start the second pointer from the second element
        for j in range(1, len(nums)):
            # If current element is different from the last unique element
            if nums[j] != nums[i]:
                # Move the unique element to the position i+1
                i += 1
                nums[i] = nums[j]

        # The length of the array with unique elements
        return i + 1

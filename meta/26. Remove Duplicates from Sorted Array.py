from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize the first pointer. Pointer write_pointer keeps track of the position in the array
        # where the next unique element should be placed.
        write_pointer = 0

        # Start the second pointer from the second element
        for read_pointer in range(1, len(nums)):
            # If current element is different from the last unique element
            if nums[read_pointer] != nums[write_pointer]:
                # Move the unique element to the position write_pointer+1
                write_pointer += 1
                nums[write_pointer] = nums[read_pointer]

        # The length of the array with unique elements
        return write_pointer + 1

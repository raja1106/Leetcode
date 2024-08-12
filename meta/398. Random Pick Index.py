import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        result = -1
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                count += 1
                if random.randint(1, count) == count:
                    result = i
        return result

class Solution1:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0  # Counter for the occurrence of the target
        chosen_index = None  # Variable to store the randomly chosen index

        # Enumerate over the list of numbers
        for index, value in enumerate(self.nums):
            # Check if the current value matches the target
            if value == target:
                count += 1  # Increment the counter for each occurrence
                # Generate a random number between 1 and the current count (both inclusive)
                random_number = random.randint(1, count)
                # If the generated number equals the current count, update the chosen index
                if random_number == count:
                    chosen_index = index
        # Return the selected index which corresponds to the target in the list
        return chosen_index

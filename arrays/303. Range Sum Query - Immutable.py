from itertools import accumulate
from typing import List
class NumArray:
    def __init__(self, nums: List[int]):
        # Pre-calculate the cumulative sum of the array.
        # The 'initial=0' makes sure the sum starts from index 0 for easier calculations.
        self.cumulative_sum = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        # Calculate the sum of elements between 'left' and 'right'
        # by subtracting the sum up to 'left' from the sum up to 'right + 1'.'
        if left == 0:
            return self.cumulative_sum[right]
        return self.cumulative_sum[right] - self.cumulative_sum[left-1]




nums = [1, 2, 3, 4, 5]
cumulative_sums = accumulate(nums)

print(list(cumulative_sums))

import sys
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum_length_map = {0: 0}
        current_prefix_sum = 0
        max_subarray_length = 0

        for current_index in range(len(nums)):
            current_prefix_sum += nums[current_index]

            if current_prefix_sum - k in prefix_sum_length_map:
                max_subarray_length = max(max_subarray_length,
                                          current_index + 1 - prefix_sum_length_map[current_prefix_sum - k])

            if current_prefix_sum not in prefix_sum_length_map:
                prefix_sum_length_map[current_prefix_sum] = current_index + 1

        return max_subarray_length


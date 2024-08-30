import sys
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum_map = {0: 0}
        prefix_sum = 0
        max_subarray_length = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum - k in prefix_sum_map:
                max_subarray_length = max(max_subarray_length,
                                          i + 1 - prefix_sum_map[prefix_sum - k])

            if prefix_sum not in prefix_sum_map:
                prefix_sum_map[prefix_sum] = i + 1

        return max_subarray_length


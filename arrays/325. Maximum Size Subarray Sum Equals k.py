import sys
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum_to_index = {0: 0}
        prefix_sum = 0
        max_value = 0
        for i in range(len(nums)):
            prefix_sum = prefix_sum + nums[i]
            if prefix_sum - k in sum_to_index:
                max_value = max(max_value, i + 1 - sum_to_index[prefix_sum - k])
            if prefix_sum not in sum_to_index:
                sum_to_index[prefix_sum] = i

        return max_value

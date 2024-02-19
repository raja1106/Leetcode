import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left, window_sum = 0, 0

        global_min = math.inf
        for i in range(len(nums)):
            window_sum += nums[i]
            while (left <= i and window_sum >= target):
                global_min = min(global_min, i - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if global_min == math.inf else global_min
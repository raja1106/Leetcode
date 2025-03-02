import sys
from typing import List

from typing import List
from collections import defaultdict


class Solution_Best_Solution:
    def maxSubArrayLen(self, arr: List[int], k: int) -> int:
        """
        Find the longest subarray [j...i] whose sum equals k.
        We track prefix sums and look for previous prefix_sums[i] - k.
        """
        prefix_sums = defaultdict(int)  # Stores first occurrence of each prefix sum
        prefix_sums[0] = -1  # Needed to handle sum exactly equal to k at the beginning
        running_sum = 0
        longest_subarray = 0

        for i in range(len(arr)):
            running_sum += arr[i]

            # Check if a subarray sum equals k
            if running_sum - k in prefix_sums:
                longest_subarray = max(longest_subarray, i - prefix_sums[running_sum - k])

            # Store first occurrence of running_sum
            if running_sum not in prefix_sums:
                prefix_sums[running_sum] = i # i denotes index here

        return longest_subarray


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum_map = {0: 0}
        prefix_sum = 0
        max_subarray_length = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum - k in prefix_sum_map:
                max_subarray_length = max(max_subarray_length, (i + 1) - prefix_sum_map[prefix_sum - k])
                #prefix_sum_map[prefix_sum - k] is length of yellow array [0...j-1]
            if prefix_sum not in prefix_sum_map:
                prefix_sum_map[prefix_sum] = i+1  # i + 1 denotes length of current array [0,1,..i]"prefix_sum"

        return max_subarray_length
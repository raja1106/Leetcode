from typing import List

"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

"""


# 2,5,5,0,2   k=7
class Solution:
    from typing import List

    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize hashmap to store the frequency of prefix sums
        prefix_sum_count = {0: 1}
        prefix_sum = 0
        count = 0

        # Iterate through the list of numbers
        for num in nums:
            # Update the prefix sum
            prefix_sum += num

            # Check if there is a prefix sum that, when subtracted from the current prefix sum, equals k
            if prefix_sum - k in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]

            # Update the hashmap with the current prefix sum
            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum] += 1
            else:
                prefix_sum_count[prefix_sum] = 1

        return count

    def subarraySumUsingCounter(self, nums: List[int], k: int) -> int:
        prefix_sum_count = Counter()
        prefix_sum_count[0] = 1
        prefix_sum = 0
        total_count = 0
        for i in range(len(nums)):
            # Update the prefix sum
            prefix_sum += nums[i]

            # Check if there is a prefix sum that, when subtracted from the current prefix sum, equals k
            if prefix_sum - k in prefix_sum_count:
                total_count += prefix_sum_count[prefix_sum - k]

            # Update the Counter with the current prefix sum
            prefix_sum_count[prefix_sum] += 1

        return total_count

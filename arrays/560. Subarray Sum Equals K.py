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
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = {}
        hmap[0] = 1
        prefixSum = 0
        globalCount = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            if prefixSum - k in hmap:
                globalCount += hmap[prefixSum - k]

            if prefixSum in hmap:
                hmap[prefixSum] += 1
            else:
                hmap[prefixSum] = 1

        return globalCount

    def subarraySumUsingCounter(self, nums: List[int], k: int) -> int:
        sum_frequency = Counter()
        sum_frequency[0] = 1
        prefix_sum = 0
        total_count = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in sum_frequency:
                total_count += sum_frequency[prefix_sum - k]
            sum_frequency[prefix_sum] += 1

        return total_count

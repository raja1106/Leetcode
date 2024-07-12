import heapq
from typing import List
from collections import Counter

"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_count = Counter(nums) # map (num-> freq)
        print(element_count)
        ans= self.quick_select(nums,list(element_count.items()),0,len(element_count)-1,k)

        result = [val for val in ans]

    def quick_select(self, nums_freq, start, end, k):
        partition_idx = self.partition(nums_freq, start, end)
        if partition_idx == len(nums_freq)-k:
            return nums_freq[partition_idx:]
        else:
            return self.quick_select(nums_freq, partition_idx + 1, end, k)


    def partition(self, nums_freq, start, end):
        rand_index = random.randint(start, end)
        nums_freq[rand_index], nums_freq[start] = nums_freq[start], nums_freq[rand_index]
        pivot =start
        left = start+1
        right =end

        while left <= right:
            if nums_freq[right] < nums_freq[pivot] <nums_freq[left]:
                nums_freq[right], nums_freq[left] = nums_freq[left], nums_freq[right]
                left += 1
                right -=1
            if nums_freq[left] <= nums_freq[pivot]:
                left += 1
            if nums_freq[right] >= nums_freq[pivot]:
                right -=1

        nums_freq[right], nums_freq[pivot] = nums_freq[pivot], nums_freq[right]
        return right





    def topKFrequentUsingMinHeap(self, nums: List[int], k: int) -> List[int]: #T(n)=O(n log k)
        element_count = Counter(nums)
        min_heap = []
        for num, freq in element_count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [pair[1] for pair in min_heap]


obj = Solution()
arr=[1,1,1,2,2,3]
print(obj.topKFrequent(arr,2))

"""
Time Complexity
The time complexity of the function is determined by several factors:

Counting Elements: The function begins with cnt = Counter(nums) which counts the frequency of each element in the nums array. Constructing this frequency counter takes O(N) time, where N is the number of elements in nums.

Heap Operations: The function then involves a for loop, iterating over the frequency counter's items, and performing heap operations. For each unique element (up to N unique elements), a heap push is performed, which has a time complexity of O(log K), as the size of the heap is maintained at k. In the worst case, there are N heap push and pop operations, each taking O(log K) time. Therefore, the complexity due to heap operations is O(N * log K).

The resulting overall time complexity is O(N + N * log K). However, since N * log K is the dominant term, we consider the overall time complexity to be O(N * log K).
"""
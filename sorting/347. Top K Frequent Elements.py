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

import random
from collections import Counter
from typing import List, Tuple


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        element_count = Counter(nums)

        # Convert the frequency dictionary to a list of tuples (num, freq)
        freq_list = list(element_count.items())

        # Step 2: Use quick select to find the top k frequent elements
        self.quick_select(freq_list, 0, len(freq_list) - 1, len(freq_list) - k)

        # Step 3: Extract the elements from the top k frequent tuples
        result = [val for val, freq in freq_list[-k:]]

        return result

    def quick_select(self, nums_freq: List[Tuple[int, int]], left: int, right: int, k: int):
        if left < right:
            pivot_index = self.partition(nums_freq, left, right)
            if pivot_index == k:
                return
            elif pivot_index < k:
                self.quick_select(nums_freq, pivot_index + 1, right, k)
            else:
                self.quick_select(nums_freq, left, pivot_index - 1, k)

    def partition(self, nums_freq: List[Tuple[int, int]], left: int, right: int) -> int:
        pivot_index = random.randint(left, right)
        pivot_frequency = nums_freq[pivot_index][1]
        # Move pivot to end
        nums_freq[pivot_index], nums_freq[right] = nums_freq[right], nums_freq[pivot_index]
        store_index = left
        for i in range(left, right):
            if nums_freq[i][1] < pivot_frequency:
                nums_freq[store_index], nums_freq[i] = nums_freq[i], nums_freq[store_index]
                store_index += 1
        # Move pivot to its final place
        nums_freq[right], nums_freq[store_index] = nums_freq[store_index], nums_freq[right]
        return store_index

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
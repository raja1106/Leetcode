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

from collections import Counter


class Solution_bucket_sort: #Best_one O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)  # O(n)
        max_freq = max(freq_map.values())

        # Create buckets: index represents frequency
        buckets = [[] for _ in range(max_freq + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        result = []
        # Traverse buckets from highest frequency to lowest
        for freq in range(max_freq, 0, -1):
            # for num in buckets[freq]:
            result.extend(buckets[freq])
            if len(result) >= k:
                return result[:k]


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

import random
from collections import Counter
from typing import List


class Solution_latest_quick_select:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the top k frequent elements in nums using QuickSelect.
        """

        def partition(start, end):
            pivot_index = random.randint(start, end)
            frequency_list[start], frequency_list[pivot_index] = frequency_list[pivot_index], frequency_list[start]
            pivot = start
            left, right = start + 1, end

            while left <= right:
                if frequency_list[left] > frequency_list[pivot] and frequency_list[right] < frequency_list[pivot]:
                    frequency_list[left], frequency_list[right] = frequency_list[right], frequency_list[left]
                    left += 1
                    right -= 1
                if frequency_list[left] <= frequency_list[pivot]:
                    left += 1
                if frequency_list[right] >= frequency_list[pivot]:
                    right -= 1

            frequency_list[pivot], frequency_list[right] = frequency_list[right], frequency_list[pivot]
            return right

        def quick_select(start, end):
            partition_index = partition(start, end)
            if partition_index == len(frequency_list) - k:
                return frequency_list[partition_index:]
            elif partition_index < len(frequency_list) - k:
                return quick_select(partition_index + 1, end)
            else:
                return quick_select(start, partition_index - 1)

        frequency_map = Counter(nums)  # Mapping of number -> frequency
        frequency_list = list(frequency_map.values())  # Extract frequency values

        top_frequencies = quick_select(0, len(frequency_list) - 1)
        top_elements = []

        for num, freq in frequency_map.items():
            if freq in top_frequencies:
                top_elements.append(num)

        return top_elements

from collections import Counter
from heapq import heappush,heappop,heapify
class Solution_Using_max_heap:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_freq = Counter(nums)
        max_heap = [(-freq,val) for val,freq in count_freq.items()]
        heapify(max_heap)
        result = []
        for _ in range(k):
            result.append(heappop(max_heap)[1])

        return result

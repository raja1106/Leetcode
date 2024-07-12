from typing import List
from collections import Counter, deque
from heapq import heapify, heappop, heappush
""""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation:
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
Example 2:

Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
"""

class MedianFinder:
    def __init__(self, k: int):
        self.k = k  # size of the sliding window
        self.small_max_heap = []  # max heap to store the smaller half of numbers
        self.large_min_heap = []  # min heap to store the larger half of numbers
        self.removed = defaultdict(int)  # count of delayed elements for lazy deletion
        self.small_size = 0  # size of small_max_heap (not necessarily len(small_max_heap))
        self.large_size = 0  # size of large_min_heap (not necessarily len(large_min_heap))

    def add_num(self, num: int):
        # Add a number to one of the heaps
        if not self.small_max_heap or num <= -self.small_max_heap[0]:
            heappush(self.small_max_heap, -num)
            self.small_size += 1
        else:
            heappush(self.large_min_heap, num)
            self.large_size += 1
        self.rebalance()

    def find_median(self) -> float:
        # Find the median of the current numbers
        return -self.small_max_heap[0] if self.k % 2 == 1 else (-self.small_max_heap[0] + self.large_min_heap[0]) / 2

    def remove_num(self, num: int):
        # Lazily remove a number (the number will be removed later during pruning)
        self.removed[num] += 1
        if num <= -self.small_max_heap[0]:
            self.small_size -= 1
            if num == -self.small_max_heap[0]:
                self.prune_max_heap(self.small_max_heap)
        else:
            self.large_size -= 1
            if num == self.large_min_heap[0]:
                self.prune_min_heap(self.large_min_heap)
        self.rebalance()

    def prune_min_heap(self, heap: List[int]):
        # Remove elements that have been flagged for removal
        while heap and self.removed[heap[0]] > 0:
            self.removed[heap[0]] -= 1
            if self.removed[heap[0]] == 0:
                del self.removed[heap[0]]
            heappop(heap)

    def prune_max_heap(self, heap: List[int]):
        # Remove elements that have been flagged for removal
        while heap and self.removed[-heap[0]] > 0:
            self.removed[-heap[0]] -= 1
            if self.removed[-heap[0]] == 0:
                del self.removed[-heap[0]]
            heappop(heap)

    def rebalance(self):
        # Balance the two heaps to maintain the invariant small_max_heap.size() > large_min_heap.size()
        while self.small_size > self.large_size + 1:
            heappush(self.large_min_heap, -heappop(self.small_max_heap))
            self.small_size -= 1
            self.large_size += 1
            self.prune_max_heap(self.small_max_heap)
        while self.small_size < self.large_size:
            heapq.heappush(self.small_max_heap, -heapq.heappop(self.large_min_heap))
            self.large_size -= 1
            self.small_size += 1
            self.prune_min_heap(self.large_min_heap)
class Solution:

    def median_sliding_window(self, nums: List[int], k: int) -> List[float]:
        finder = MedianFinder(k)
        for x in nums[:k]:
            finder.add_num(x)
        medians = [finder.find_median()]
        for i in range(k, len(nums)):
            finder.add_num(nums[i])
            finder.remove_num(nums[i - k])
            medians.append(finder.find_median())
        return medians











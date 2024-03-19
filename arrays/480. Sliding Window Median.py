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
                self.prune(self.small_max_heap)
        else:
            self.large_size -= 1
            if num == self.large_min_heap[0]:
                self.prune(self.large_min_heap)
        self.rebalance()

    def _prune(self, heap: List[int]):
        # Remove elements that have been flagged for removal
        while heap and self.removed[heap[0]] > 0:
            self.removed[heap[0]] -= 1
            if self.removed[heap[0]] == 0:
                del self.removed[heap[0]]
            heappop(heap)

    def _rebalance(self):
        # Balance the two heaps to maintain the invariant small_max_heap.size() > large_min_heap.size()
        while self.small_size > self.large_size + 1:
            heappush(self.large_min_heap, -heappop(self.small_max_heap))
            self.small_size -= 1
            self.large_size += 1
            self.prune(self.small_max_heap)
        while self.small_size < self.large_size:
            heapq.heappush(self.small_max_heap, -heapq.heappop(self.large_min_heap))
            self.large_size -= 1
            self.small_size += 1
            self.prune(self.large_min_heap)
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


    def medianSlidingWindow_medium(self, nums: List[int], k: int) -> List[float]:
        result = []
        max_heap, min_heap = [], []
        removed_set = set()
        self.max_heap_size, self.min_heap_size = 0, 0

        for i, num in enumerate(nums):
            self._add_number(max_heap, min_heap, num, i, removed_set)

            if i < k - 1:
                continue

            if i > k - 1:
                self._delete_number(max_heap, min_heap, removed_set, nums[i - k], i - k)

            self._balance(max_heap, min_heap, removed_set)
            self._pop_removed_items(max_heap, min_heap, removed_set)
            if self.max_heap_size == self.min_heap_size + 1:
                median = -max_heap[0][0]
            else:
                median = (-max_heap[0][0] + min_heap[0][0]) / 2
            result.append(median)

        return result

    def _add_number(self, max_heap, min_heap, number, index, removed_set):
        self._pop_removed_items(max_heap, min_heap, removed_set)
        if not max_heap or (number, index) <= (-max_heap[0][0], -max_heap[0][1]):
            heappush(max_heap, (-number, -index))
            self.max_heap_size += 1
        else:
            heappush(min_heap, (number, index))
            self.min_heap_size += 1

    def _delete_number(self, max_heap, min_heap, removed_set, number, index):
        # it's guaranteed that max_heap is not empty
        self._pop_removed_items(max_heap, min_heap, removed_set)
        if (number, index) <= (-max_heap[0][0], -max_heap[0][1]):
            removed_set.add((-number, -index))
            self.max_heap_size -= 1
        else:
            removed_set.add((number, index))
            self.min_heap_size -= 1

    def _balance(self, max_heap, min_heap, removed_set):
        # at most one iteration in one of the while loops will be executed
        while self.max_heap_size > self.min_heap_size + 1:
            self._pop_removed_items(max_heap, min_heap, removed_set)

            negative_number, negative_index = heappop(max_heap)
            self.max_heap_size -= 1

            heappush(min_heap, (-negative_number, -negative_index))
            self.min_heap_size += 1

        while self.max_heap_size < self.min_heap_size:
            self._pop_removed_items(max_heap, min_heap, removed_set)

            number, index = heappop(min_heap)
            self.min_heap_size -= 1

            heappush(max_heap, (-number, -index))
            self.max_heap_size += 1

    def _pop_removed_items(self, max_heap, min_heap, removed_set):
        while max_heap and max_heap[0] in removed_set:
            heappop(max_heap)

        while min_heap and min_heap[0] in removed_set:
            heappop(min_heap)







    def medianSlidingWindow_I(self, nums: List[int], k: int) -> List[float]:
        if not nums or not k:
            return []
        max_heap = []
        min_heap = []

        for i in range(k):
            if len(max_heap) == len(min_heap):
                heapq.heappush(min_heap, -heapq.heappushpop(max_heap, -nums[i]))
            else:
                heapq.heappush(max_heap, -heapq.heappushpop(min_heap, nums[i]))

        ans = [float(min_heap[0])] if k & 1 else [(min_heap[0] - max_heap[0]) / 2.0]

        to_remove = defaultdict(int)

        for i in range(k, len(nums)): # right bound of window

            heapq.heappush(max_heap, -heapq.heappushpop(min_heap, nums[i])) # always push to lo

            out_num = nums[i-k]
            if out_num > -max_heap[0]:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            to_remove[out_num] += 1
            while max_heap and to_remove[-max_heap[0]]:
                to_remove[-max_heap[0]] -= 1
                heapq.heappop(max_heap)
            while to_remove[min_heap[0]]:
                to_remove[min_heap[0]] -= 1
                heapq.heappop(min_heap)
            if k % 2:
                ans.append(float(min_heap[0]))
            else:
                ans.append((min_heap[0] - max_heap[0]) / 2.0)
        return ans











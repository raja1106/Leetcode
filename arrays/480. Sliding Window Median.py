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
        self.left_heap = []  # max heap to store the smaller half of numbers
        self.right_heap = []  # min heap to store the larger half of numbers
        self.pending_removals = defaultdict(int)  # count of delayed elements for lazy deletion
        self.left_size = 0  # size of left_heap (not necessarily len(left_heap))
        self.right_size = 0  # size of right_heap (not necessarily len(right_heap))

    def add_num(self, num: int):
        # Add a number to one of the heaps
        if not self.left_heap or num <= -self.left_heap[0]:
            heappush(self.left_heap, -num)
            self.left_size += 1
        else:
            heappush(self.right_heap, num)
            self.right_size += 1
        self._rebalance_heaps()

    def find_median(self) -> float:
        # Find the median of the current numbers
        return -self.left_heap[0] if self.k % 2 == 1 else (-self.left_heap[0] + self.right_heap[0]) / 2

    def delete_num(self, num: int):
        # Lazily remove a number (the number will be pending_removals later during pruning)
        self.pending_removals[num] += 1
        if num <= -self.left_heap[0]:
            self.left_size -= 1
            if num == -self.left_heap[0]:
                self._prune_left_heap(self.left_heap)
        else:
            self.right_size -= 1
            if num == self.right_heap[0]:
                self._prune_right_heap(self.right_heap)
        self._rebalance_heaps()

    def _prune_right_heap(self, heap: List[int]):
        # Remove elements that have been flagged for removal
        while heap and self.pending_removals[heap[0]] > 0:
            self.pending_removals[heap[0]] -= 1
            if self.pending_removals[heap[0]] == 0:
                del self.pending_removals[heap[0]]
            heappop(heap)

    def _prune_left_heap(self, heap: List[int]):
        # Remove elements that have been flagged for removal
        while heap and self.pending_removals[-heap[0]] > 0:
            self.pending_removals[-heap[0]] -= 1
            if self.pending_removals[-heap[0]] == 0:
                del self.pending_removals[-heap[0]]
            heappop(heap)

    def _rebalance_heaps(self):
        # Balance the two heaps to maintain the invariant left_heap.size() > right_heap.size()
        while self.left_size > self.right_size + 1:
            heappush(self.right_heap, -heappop(self.left_heap))
            self.left_size -= 1
            self.right_size += 1
            self._prune_left_heap(self.left_heap)
        while self.left_size < self.right_size:
            heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))
            self.right_size -= 1
            self.left_size += 1
            self._prune_right_heap(self.right_heap)
class Solution:

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        finder = MedianFinder(k)
        for x in nums[:k]:
            finder.add_num(x)
        medians = [finder.find_median()]
        for i in range(k, len(nums)):
            finder.add_num(nums[i])
            finder.delete_num(nums[i - k])
            medians.append(finder.find_median())
        return medians

from typing import List
from sortedcontainers import SortedList


class Solution_using_SortedList:#similer to TreeMap
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 0 or not nums:
            return []

        window = SortedList(nums[:k])
        result: List[float] = []

        def get_median() -> float:
            mid = k // 2
            if k & 1:
                # odd k → middle element
                return float(window[mid])
            # even k → average two middles
            return (window[mid - 1] + window[mid]) / 2

        # first window’s median
        result.append(get_median())

        # slide the window
        for i in range(k, len(nums)):
            # remove the element going out
            window.remove(nums[i - k])
            # add the new element
            window.add(nums[i])
            # record median
            result.append(get_median())

        return result


class Solution_Using_Deque:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = deque(nums[:k])
        sorted_window = sorted(window)
        result = []
        if len(sorted_window) % 2 == 0:  # 4-->  1,2
            val = (sorted_window[k // 2] + sorted_window[(k // 2) - 1]) / 2
            result.append(val)
        else:
            val = sorted_window[k // 2]
            result.append(val)

        for i in range(k, len(nums)):
            window.popleft()
            window.append(nums[i])
            if len(window) == k:
                sorted_window = sorted(window)
                if len(sorted_window) % 2 == 0:  # 4-->  1,2
                    val = (sorted_window[k // 2] + sorted_window[(k // 2) - 1]) / 2
                    result.append(val)
                else:
                    val = sorted_window[k // 2]
                    result.append(val)

        return result










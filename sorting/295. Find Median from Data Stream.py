import heapq

class MedianFinder:
    def __init__(self):
        self.smaller_max_heap = []  # Max heap (store negative values)
        self.larger_min_heap = []  # Min heap (store positive values)

    def addNum(self, num: int) -> None:
        # If both heaps are empty, insert into smaller_max_heap first
        if not self.smaller_max_heap or num <= -self.smaller_max_heap[0]:
            heapq.heappush(self.smaller_max_heap, -num)
        else:
            heapq.heappush(self.larger_min_heap, num)

        # Balance the heaps
        if len(self.smaller_max_heap) > len(self.larger_min_heap) + 1:
            heapq.heappush(self.larger_min_heap, -heapq.heappop(self.smaller_max_heap))
        elif len(self.larger_min_heap) > len(self.smaller_max_heap):
            heapq.heappush(self.smaller_max_heap, -heapq.heappop(self.larger_min_heap))

    def findMedian(self) -> float:
        if len(self.smaller_max_heap) > len(self.larger_min_heap):
            return -self.smaller_max_heap[0]
        elif len(self.smaller_max_heap) < len(self.larger_min_heap):
            return self.larger_min_heap[0]
        else:
            return (-self.smaller_max_heap[0] + self.larger_min_heap[0]) / 2.0


# Example Usage:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

from heapq import heappush, heappop, heappushpop


class MedianFinder_May_2025:

    def __init__(self):
        self.left_heap = []  # max_heap
        self.right_heap = []  # min_heap
        self.size = 0

    def rebalance(self):
        if len(self.left_heap) > len(self.right_heap) + 1:
            element = -heappop(self.left_heap)
            heappush(self.right_heap, element)
        elif len(self.right_heap) > len(self.left_heap):
            element = heappop(self.right_heap)
            heappush(self.left_heap, -element)

    def addNum(self, num: int) -> None:
        if not self.left_heap or -self.left_heap[0] >= num:
            heappush(self.left_heap, -num)
        else:
            heappush(self.right_heap, num)
        self.rebalance()
        self.size += 1

    def findMedian(self) -> float:
        n = self.size
        if n % 2 == 1:
            return -self.left_heap[0]
        else:
            return (-self.left_heap[0] + self.right_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

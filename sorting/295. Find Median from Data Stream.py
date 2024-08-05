import heapq


class MedianFinder:

    def __init__(self):
        self.small_max_heap = [] #max heap
        self.large_min_heap = [] #min heap

    def addNum(self, num: int) -> None:
        if self.large_min_heap and num > self.large_min_heap[0]:
            heapq.heappush(self.large_min_heap, num)
        else:
            heapq.heappush(self.small_max_heap, -1 * num)
        if len(self.small_max_heap) > len(self.large_min_heap) +1:
            val = -1* heapq.heappop(self.small_max_heap)
            heapq.heappush(self.large_min_heap, val)
        if len(self.large_min_heap) > len(self.small_max_heap)+1:
            val = heapq.heappop(self.large_min_heap)
            heapq.heappush(self.small_max_heap, -1 * val)

    def findMedian(self) -> float:
        if len(self.small_max_heap) > len(self.large_min_heap):
            return -1*self.small_max_heap[0]
        elif len(self.small_max_heap) < len(self.large_min_heap):
            return self.large_min_heap[0]
        else:
            return (self.large_min_heap[0] + (-1 * self.small_max_heap[0])) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
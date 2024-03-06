import heapq
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        max_heap = []

        for x,y in points:
            heapq.heappush(max_heap,(- x * x - y * y, [x, y]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [pair[1] for pair in max_heap]












obj = Solution()
obj.kClosest([[1,3],[-2,2]],1)
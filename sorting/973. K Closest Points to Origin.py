import heapq
from typing import List
class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return -1 * (point[0] ** 2 + point[1] ** 2)

        max_heap = []
        result = []
        for i in range(len(points)):
            heapq.heappush(max_heap, (distance(points[i]), points[i]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [pair[1] for pair in max_heap]

    def kClosest_usingforloop(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return -1 * (point[0] ** 2 + point[1] ** 2)

        max_heap = []
        result = []
        for i in range(len(points)):
            heapq.heappush(max_heap, (distance(points[i]), points[i]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        for x, y in max_heap:
            result.append(y)
            """
            or you can in below way also
            for x in max_heap:
             result.append(x[1])
             """
        return result
    def kClosest_walkqq(self, points: List[List[int]], k: int) -> List[List[int]]:

        max_heap = []

        for x,y in points:
            heapq.heappush(max_heap,(- x * x - y * y, [x, y]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [pair[1] for pair in max_heap]

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return None










obj = Solution()
obj.kClosest([[1,3],[-2,2]],1)
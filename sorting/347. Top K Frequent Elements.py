import heapq
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_count = Counter(nums)
        min_heap =[]
        for key in element_count:
            v=element_count[key]
            heapq.heappush(min_heap,(v,key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [pair[1] for pair in min_heap]


obj = Solution()
arr=[1,1,1,2,2,3]
print(obj.topKFrequent(arr,2))
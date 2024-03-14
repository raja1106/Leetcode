from typing import List


import heapq
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            while i != nums[i]:
                d = nums[i]

                if d<len[nums]:
                    nums[d],nums[i]=nums[i],nums[d]
                else:
                    break



        return nums

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0]**2 + point[1]**2
        max_heap =[]
        result=[]
        for i in range(len(points)):
            heapq.heappush((distance(points[i]),points[i]))
            if len(max_heap) > k:
                max_heap.pop()

        for element in max_heap:
            result.append(element[1])






obj=Solution()
print(obj.test([2,3,4,5]))


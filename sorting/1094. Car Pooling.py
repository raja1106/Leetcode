import heapq
from typing import List
class Solution: #TODOO with correct custom minheap approach
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        required_capacity=0
        min_heap =[]

        for i in range(len(trips)):
            while min_heap and min_heap[0][0] <= trips[i][1]:
                required_capacity -= heapq.heappop(min_heap)[1]

            required_capacity +=  trips[i][0]

            heapq.heappush(min_heap,(trips[i][2],trips[i][0]))

            if required_capacity > capacity:
                return False

        return True

    def carPoolingWorking(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        car_people = 0
        min_heap =[] # heapq.heappush(max_heap,(- x * x - y * y, [x, y]))

        for i in range(len(trips)):
            if i == len(trips)-1:
                nextstart =float('inf')
            else:
                nextstart = trips[i+1][1]
            heapq.heappush(min_heap,(trips[i][2],trips[i][0]))
            car_people +=  trips[i][0]

            if car_people > capacity:
                return False

            while min_heap and min_heap[0][0] <= nextstart:
                required_capacity -= heapq.heappop(min_heap)[0]

        return True



class SolutionWorking:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        heap = [(-1, 0)]
        for trip in trips:
            while heap and trip[1] >= heap[0][0]:
                last_end, last_num = heappop(heap)
                capacity += last_num
            heappush(heap, (trip[2], trip[0]))
            if capacity - trip[0] >= 0:
                capacity -= trip[0]
            else:
                return False
        return True

obj = Solution()
print(obj.carPooling([[9,0,1],[3,3,7]],4))
import heapq
class Solution: #TODOO with correct custom minheap approach
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        required_capacity=trips[0][0]
        min_heap =[trips[0]] # heapq.heappush(max_heap,(- x * x - y * y, [x, y]))

        for i in range(1,len(trips)):
            while min_heap and min_heap[0][2] <= trips[i][1]:
                required_capacity -= heapq.heappop(min_heap)[0]

            required_capacity +=  trips[i][0]

            heapq.heappush(min_heap,trips[i])

            if required_capacity > capacity:
                return False

        return True
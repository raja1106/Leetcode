from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result =[]

        min_heap = [[v+nums2[0],i,0] for i,v in enumerate(nums1[:k])]
        heapify(min_heap)

        while min_heap and len(result) < k:
            sum_pair,index1,index2 = heappop(min_heap)

            result.append([nums1[index1],nums2[index2]])

            if index2+1 <len(nums2):
                heappush(min_heap,[nums1[index1] + nums2[index2 + 1], index1, index2 + 1])

        return result


'''
Time Complexity
The time complexity of the algorithm is as follows:

Heap Initialization: The code creates a min-heap and initializes it with the sums of elements from nums1 and the first element of nums2. Since the heap is initialized with at most k elements (and not more than the length of nums1), the complexity of this step is O(k) since each heap insertion is O(log k) and we do it at most k times.

Heap Operations: Then, in each iteration, the algorithm pops an element from the heap and potentially pushes a new element into the heap. Since we perform k iterations (bounded by k and the length of the output), and both heappop and heappush operations have a time complexity of O(log k), the complexity for this part is O(k log k).

Overall, the time complexity is O(k) + O(k log k), which simplifies to O(k log k) because as k grows, the k log k term dominates.

Space Complexity
The space complexity of the algorithm is as follows:

Heap Space: The heap size is at most k, as it stores pairs of indices and their corresponding sum, giving us O(k).

Output List: The list ans to store the answer pairs. In the worst case, it will contain k pairs, leading to O(k) space complexity.

The overall space complexity combines the heap space and the output list, but since both are O(k), the total space complexity remains O(k).

'''


def kSmallestPairsUsingMaxHeap(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]: #This is not working
        result = []
        min_heap = [[nums1[0]+v, [nums1[0], v]] for i, v in enumerate(nums2[:k])]
        heapify(min_heap)
        i=1
        j=0
        while i<len(nums1) and j<len(nums2):
            if len(min_heap) < k:
               heappush(min_heap,[nums1[i]+nums2[j],[nums1[i],nums2[j]]])
               continue

            if nums1[i]+nums2[j]>min_heap[0][0]:
                break
            else:
                heappop(min_heap)
                heappush(min_heap, [nums1[i] + nums2[j], [nums1[i], nums2[j]]])

        while min_heap:
            result.append(heappop(min_heap))
        return result
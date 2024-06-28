import heapq
import collections.deque
from sortedcontainers import SortedList

class Solution:
    #Input: nums = [8,2,4,7], limit = 4
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left=0
        max_length=0
        minQueue, maxQueue = collections.deque(), collections.deque()
        for i in range(len(nums)):

            while minQueue and minQueue[-1] > nums[i]:
                minQueue.pop()
            minQueue.append(nums[i])

            while maxQueue and maxQueue[-1] < nums[i]:
                maxQueue.pop()
            maxQueue.append(nums[i])

            while left <= i and maxQueue[0]-minQueue[0] > limit:
                if nums[left] == minQueue[0]:
                    minQueue.popleft()
                if nums[left] == maxQueue[0]:
                    maxQueue.popleft()
                left += 1

            max_length = max(max_length,i-left+1)
        return max_length

    def longestSubarrayUsingSOrtedList(self, nums: List[int], limit: int) -> int:
        sorted_list = SortedList()
        max_length=0
        left=0

        for i,value in enumerate(nums):
            sorted_list.add(value)

            while left <= i and sorted_list[-1]-sorted_list[0] > limit:

                sorted_list.remove(nums[left])
                left += 1

            max_length =max(max_length,i-left+1)
            #max_length =max(max_length,len(sorted_list))
        return max_length
import heapq

class Solution:
    #Input: nums = [8,2,4,7], limit = 4
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left=0
        max_length=0
        min_heap=[]
        max_heap=[]
        for i in range(len(nums)):

            heapq.heappush(min_heap,nums[i])
            heapq.heappush(max_heap, -nums[i])
            min_value = min_heap[0]
            max_value = -max_heap[0]

            while left <= i and max_value-min_value > limit:
                heapq.heapreplace()
                min_heap.pop(nums[left])
                max_heap.pop(nums[left])
                min_value = min_heap[0]
                max_value = -max_heap[0]
                left += 1

            max_length = max(max_length,i-left+1)
        return max_length
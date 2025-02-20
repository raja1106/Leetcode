from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: #T(n)=O(n) worst case: O(n**2)
        if len(nums)-k < 0:
            return -1
        ans =self.quick_select(nums,0,len(nums)-1,k)
        return ans

    def quick_select(self,nums:List[int],start: int, end: int,k: int)->int:
        partition_idx = self.partition(nums, start, end)
        if partition_idx == len(nums)-k:
            return nums[partition_idx]
        elif partition_idx < len(nums)-k:
            return self.quick_select(nums,partition_idx+1,end,k)
        else:
            return self.quick_select(nums, start, partition_idx - 1,k)

    def partition(self, nums: List[int],start: int, end: int) -> int:
        rand_index = random.randint(start, end)
        nums[rand_index], nums[start] = nums[start], nums[rand_index]
        pivot =start
        left = start+1
        right =end

        while left <= right:
            if nums[right] < nums[pivot] <nums[left]:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                right -=1
            if nums[left] <= nums[pivot]:
                left += 1
            if nums[right] >= nums[pivot]:
                right -=1

        nums[right], nums[pivot] = nums[pivot], nums[right]
        return right

    from heapq import heappush, heappop, heappushpop
    from typing import List

    class Solution_Using_Min_heap:
        def findKthLargest(self, nums: List[int], k: int) -> int:
            min_heap = []

            for num in nums:
                if len(min_heap) < k:
                    heappush(min_heap, num)  # Add until heap size reaches k
                else:
                    heappushpop(min_heap, num)  # Push num and pop the smallest if needed

            return min_heap[0]  # The root of the heap is the Kth largest element

    def findKthLargestUsingMaxHeap(self, nums: List[int], k: int) -> int: # T(n)= O(klogn)
        max_heap = [-val for val in nums]
        heapify(max_heap)
        ans = 0
        for i in range(k):
            ans = -heappop(max_heap)

        return ans


class Solution_Quick_Select:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Input: nums = [3,2,1,5,6,4], k = 2

        """

        def partition(start, end):
            rand_idx = random.randint(start, end)
            nums[start], nums[rand_idx] = nums[rand_idx], nums[start]
            pivot = start
            left = start + 1
            right = end
            while left <= right:
                if nums[left] > nums[pivot] and nums[right] < nums[pivot]:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                if nums[left] <= nums[pivot]:
                    left += 1
                if nums[right] >= nums[pivot]:
                    right -= 1
            nums[pivot], nums[right] = nums[right], nums[pivot]
            return right

        def quick_select(start, end):
            partion_idx = partition(start, end)
            if partion_idx == len(nums) - k:
                return nums[partion_idx]
            elif partion_idx < len(nums) - k:
                return quick_select(partion_idx + 1, end)
            else:
                return quick_select(start, partion_idx - 1)

        return quick_select(0, len(nums) - 1)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums)-k < 0:
            return -1
        ans =self.quick_select(nums,0,len(nums)-1,k)
        return ans


    def quick_select(self,nums:List[int],start: int, end: int,k: int)->int:
        partition_idx = self.partition(nums, 0, len(nums) - 1)
        if partition_idx == len(nums)-k:
            return nums[partition_idx]
        elif partition_idx < len(nums)-k:
            self.quick_select(nums,partition_idx+1,end,k)
        else:
            self.quick_select(nums, start, partition_idx - 1,k)


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
            if nums[left] < nums[pivot]:
                left += 1
            if nums[right] > nums[pivot]:
                right -=1

        nums[right], nums[pivot] = nums[pivot], nums[right]
        return right



def find_kth_largest_Using_MinHeap(nums, k): # T(n)= O(nlogk)
    k_numbers_min_heap = []

    for i in range(k):
        k_numbers_min_heap.append(nums[i])

    heapq.heapify(k_numbers_min_heap)

    for i in range(k, len(nums)):
        if nums[i] > k_numbers_min_heap[0]:
            heapq.heappop(k_numbers_min_heap)
            heapq.heappush(k_numbers_min_heap, nums[i])

    return k_numbers_min_heap[0]
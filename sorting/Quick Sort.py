import random
from typing import List
class QuickSort:
    def sort(self, nums: List[int]) -> List[int]:
        self.quicksortHelper(nums,0,len(nums)-1)
        return nums

    def quicksortHelper(self, nums: List[int],start: int,end: int):
        if start >= end:
            return

        partition_index = self.partition(nums,start,end)
        self.quicksortHelper(nums,start,partition_index-1)
        self.quicksortHelper(nums,partition_index+1,end)

    def partition(self,nums: List[int],start: int,end: int) -> int:
        rand_index = random.randint(start,end)
        nums[rand_index], nums[start] = nums[start], nums[rand_index]
        pivot = start
        left = start+1
        right =end

        while left <= right:
            if left == right:
                print(left)
            if nums[left] > nums[pivot] > nums[right]:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
            if nums[left] <= nums[pivot]:
                left += 1
            if nums[right] >= nums[pivot]:
                right -= 1
        nums[pivot], nums[right] = nums[right], nums[pivot]

        return right

    def partition_This_Also_works(array, start, end):
        rand_index = random.randint(start, end)
        array[rand_index], array[start] = array[start], array[rand_index]
        pivot = start
        left = start + 1
        right = end

        while left <= right:
            if array[left] > array[pivot] > array[right]:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
            elif array[left] <= array[pivot]:
                left += 1
            else:
                right -= 1
        array[right], array[start] = array[start], array[right]
        return right

sort = QuickSort()
print(sort.sort([8, 5, 2, 9, 5, 6, 3]))
import random
from typing import List

from typing import List
import random
from typing import List
import random


class Solution_LC912:
    def sortArray(self, nums: List[int]) -> List[int]:
        obj = QuickSortHoarePartitioning()
        return obj.sort(nums)


class QuickSortHoarePartitioning: # More Efficient
    def sort(self, nums: List[int]) -> List[int]:
        self.quicksortHelper(nums, 0, len(nums) - 1)
        return nums

    def quicksortHelper(self, nums: List[int], start: int, end: int):
        if start >= end:
            return

        partition_index = self.partition(nums, start, end)

        # Fix infinite recursion by ensuring recursive calls shrink the range
        if partition_index > start:
            self.quicksortHelper(nums, start, partition_index)  # Left part
        if partition_index + 1 < end:
            self.quicksortHelper(nums, partition_index + 1, end)  # Right part

    def partition(self, nums: List[int], start: int, end: int) -> int:
        rand_index = random.randint(start, end)
        nums[rand_index], nums[start] = nums[start], nums[rand_index]  # Swap pivot to start
        pivot = nums[start]

        left = start - 1  # Fix initialization for Hoare's partitioning
        right = end + 1

        while True:
            # Move left pointer until finding an element >= pivot
            left += 1
            while nums[left] < pivot:
                left += 1

            # Move right pointer until finding an element <= pivot
            right -= 1
            while nums[right] > pivot:
                right -= 1

            if left >= right:  # If pointers cross, partitioning is done
                return right  # Fix: return `right`, NOT `left`

            # Swap elements at left and right indices
            nums[left], nums[right] = nums[right], nums[left]


class QuickSort_Lomuto_Partitioning: # Less Efficient
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
print(sort.sort([4, 5, 2, 9, 5, 6, 3]))

# 4    2 3 5 5 9 6
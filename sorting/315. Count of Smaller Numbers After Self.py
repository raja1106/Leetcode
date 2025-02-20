from typing import List


class Solution_BruteForce:#O(n²)
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        for i in range(n):
            count = 0
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    count += 1
            result[i] = count

        return result


class Solution_Using_BinarySearch:#O(n²)
    def countSmaller(self, nums: List[int]) -> List[int]:
        st = []  # Acts as a sorted list
        result = [0] * len(nums)

        # Inner function for binary search (Find the correct insert position)
        def searchInsert(nums: List[int], target: int) -> int:
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return start  # Position to insert `target`

        # Iterate from right to left
        for i in range(len(nums) - 1, -1, -1):
            pos = searchInsert(st, nums[i])  # Find the correct position
            result[i] = pos  # The position gives the count of smaller elements
            st.insert(pos, nums[i])  # Insert `nums[i]` to maintain order

        return result


from typing import List
from sortedcontainers import SortedList

class Solution: #O(nlogn)
    def countSmaller(self, nums: List[int]) -> List[int]:
        st = SortedList()  # Acts as a sorted list
        result = [0] * len(nums)

        # Inner function for binary search (Find the correct insert position)
        def searchInsert(nums: SortedList, target: int) -> int:
            return nums.bisect_left(target)  # Find position where target should be inserted

        # Iterate from right to left
        for i in range(len(nums) - 1, -1, -1):
            pos = searchInsert(st, nums[i])  # Find the correct position O(logn)
            result[i] = pos  # The position gives the count of smaller elements
            st.add(nums[i])  # Insert nums[i] to maintain order O(logn) instead of O(n)

        return result



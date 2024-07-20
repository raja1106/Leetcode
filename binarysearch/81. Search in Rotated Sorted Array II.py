from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return True

            # If there are duplicates, we can skip them
            while start < mid and nums[start] == nums[mid]:
                start += 1
            while end > mid and nums[end] == nums[mid]:
                end -= 1

            # Determine the sorted half
            if nums[start] <= nums[mid]:  # Left half is sorted
                if nums[start] <= target < nums[mid]:  # Target in the left half
                    end = mid - 1
                else:  # Target in the right half
                    start = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[end]:  # Target in the right half
                    start = mid + 1
                else:  # Target in the left half
                    end = mid - 1

        return False

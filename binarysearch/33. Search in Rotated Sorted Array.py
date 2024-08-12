from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        if not nums:
            return -1

        # Check if the target is the last element
        if target == nums[-1]:
            return end

        # Determine which region the target belongs to
        if target < nums[-1]:
            region = "orange"
        else:
            region = "green"

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] <= nums[-1]:  # mid-lies in the "orange" region
                if nums[mid] > target or region == "green":
                    end = mid - 1
                else:
                    start = mid + 1
            else:  # mid-lies in the "green" region
                if nums[mid] < target or region == "orange":
                    start = mid + 1
                else:
                    end = mid - 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

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
        return -1

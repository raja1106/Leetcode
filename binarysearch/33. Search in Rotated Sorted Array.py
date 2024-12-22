class Solution_works_with_duplicate_values:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:  # Handle empty array
            return -1
        if target == nums[0]:
            return 0

        start = 0
        end = len(nums) - 1
        # Handle duplicates at the beginning
        while start < len(nums) and nums[start] == nums[-1]:
            start += 1

        # Binary search logic
        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            # Determine which side is sorted
            if nums[mid] >= nums[start]:  # Left side is sorted
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:  # Right side is sorted
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1

class Solution:
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
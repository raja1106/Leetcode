class Solution_template_for_search:
    def search(self, nums: List[int], target: int) -> bool:

        if not nums:  # Handle empty array
            return False
        if target == nums[0]:
            return True

        start = 0
        end = len(nums) - 1
        # Handle duplicates at the beginning
        while start < len(nums) and nums[start] == nums[-1]:
            start += 1

        # Binary search logic
        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return True

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

        return False


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        # Check if the target is the last element
        if target == nums[0]:
            return True
        if target == nums[-1]:
            return True

        left_found = None
        for i in range(len(nums)):
            if nums[i] != nums[-1]:
                left_found = i
                break
        if left_found is None:
            return False
        start = left_found
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return True

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
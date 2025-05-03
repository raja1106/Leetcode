from typing import List


class Solution:

    def singleNonDuplicate_Feb11(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        start, end = 0, len(nums) - 1
        while (start <= end):
            mid = start + (end - start) // 2
            if (nums[mid] != nums[mid + 1]) and (nums[mid] != nums[mid - 1]):
                return nums[mid]
            elif (mid % 2 == 0 and nums[mid + 1] == nums[mid]) or (mid % 2 == 1 and nums[mid - 1] == nums[mid]):
                start = mid + 1
            else:
                end = mid - 1

class Solution_April_2025:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        For even index:
            if nums[mid] == nums[mid + 1], left side is correct -> move right
            else, single element is on the left side (inclusive)
        """
        start = 0
        end = len(nums) - 1

        # Handle edge cases
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        while start <= end:
            mid = start + (end - start) // 2

            # Avoid index out of bounds safely
            if mid > 0 and mid < len(nums) - 1 and nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            # Decide the search direction
            if mid % 2 == 0:
                if mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                    start = mid + 1  # start = mid + 2 also works by skipping the confirmed pair
                else:
                    end = mid - 1
            else:
                if mid - 1 >= 0 and nums[mid] == nums[mid - 1]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1  # Should never reach here if input is valid

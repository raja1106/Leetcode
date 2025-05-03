
class Solution_Best:
    def missingElement(self, nums: List[int], k: int) -> int:
        """
        lllllLRrrrrr
        Binary Search:
        Left region  --> missing_count < k
        Right region --> missing_count >= k
        missing_count = actual_value - expected_value = nums[mid] - (nums[0] + mid)
        """
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            expected_value = nums[0] + mid
            actual_value = nums[mid]
            missing_count = actual_value - expected_value

            if missing_count < k:
                start = mid + 1
            else:
                end = mid - 1

        total_missing_until_end = nums[end] - (nums[0] + end)
        return nums[end] + (k - total_missing_until_end)

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # 4,7,9,10   k=3, ans=8
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            actual_val = nums[mid]
            predicted_val = nums[0] + mid
            missing = actual_val - predicted_val
            if missing < k:
                start = mid + 1
            else:
                end = mid - 1
        missing = nums[end] - (nums[0] + end)
        return nums[end]+(k-missing)


class Solution_With_comments:
    def missingElement(self, nums: List[int], k: int) -> int:

        # Initialize pointers for binary search
        start = 0  # Left boundary of the search space
        end = len(nums) - 1  # Right boundary of the search space
        missing = 0  # Variable to track missing elements

        # Perform binary search to locate the section where the k-th missing element falls
        while start <= end:
            # Calculate the middle index
            mid = start + (end - start) // 2

            # Calculate how many numbers are missing up to nums[mid]
            # Formula: (actual number at index mid) - (expected number at index mid)
            missing = nums[mid] - (nums[0] + mid)

            # If the number of missing elements so far is less than k,
            # it means the k-th missing element is further to the right
            if missing < k:
                start = mid + 1  # Shift search to the right
            else:
                # If missing elements exceed or equal k, the answer lies to the left
                end = mid - 1  # Narrow the search to the left
        # After the loop, 'end' points to the position where the k-th missing element falls
        # Calculate how many elements are missing up to nums[end]
        missing = nums[end] - (nums[0] + end)
        # The k-th missing element is the difference between k and the number of
        # missing elements so far, added to the last known position (nums[end])
        ans = nums[end] + (k - missing)

        return ans  # Return the k-th missing element


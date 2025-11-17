from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Step 1: Sort the array so we always "raise" smaller numbers to nums[i]
        nums.sort()

        left = 0
        max_length = 0  # This will store the max frequency
        window_sum = 0  # Sum of elements in the current window [left..i]

        for i in range(len(nums)):
            # Expand the window by including nums[i]
            window_sum += nums[i]

            # Current window size
            window_size = i - left + 1
            # Cost to make all elements in window equal to nums[i]
            # nums[i] * window_size is the sum after all raises
            cost = nums[i] * window_size - window_sum

            # While cost exceeds k, shrink from the left
            while left <= i and cost > k:
                window_sum -= nums[left]
                left += 1

                window_size = i - left + 1
                cost = nums[i] * window_size - window_sum

            # Now the window [left..i] is valid; update max_length
            max_length = max(max_length, i - left + 1)

        return max_length

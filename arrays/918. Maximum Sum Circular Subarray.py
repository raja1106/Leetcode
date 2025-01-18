from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Step 1: Find the maximum sum subarray using Kadane's algorithm
        current_max_sum = nums[0]
        global_max_sum = nums[0]
        for i in range(1, len(nums)):
            current_max_sum = max(current_max_sum + nums[i], nums[i])
            global_max_sum = max(global_max_sum, current_max_sum)

        # Step 2: Find the minimum sum subarray using Kadane's algorithm
        current_min_sum = nums[0]
        global_min_sum = nums[0]  # Track the minimum subarray sum
        total_array_sum = nums[0]
        for i in range(1, len(nums)):
            total_array_sum += nums[i]
            current_min_sum = min(current_min_sum + nums[i], nums[i])
            global_min_sum = min(global_min_sum, current_min_sum)  # Track minimum subarray

        # Step 3: Handle the case where all elements are negative
        if global_max_sum < 0:
            return global_max_sum  # If all elements are negative, return max element

        # Step 4: Return the maximum of the two possible cases
        return max(global_max_sum, total_array_sum - global_min_sum)

sol = Solution()
print(sol.maxSubarraySumCircular([1, -2, 3, -2]))  # Expected: 3 here o/p is not including circular
print(sol.maxSubarraySumCircular([5, -3, 5]))      # Expected: 10 here o/p is  including circular
print(sol.maxSubarraySumCircular([-3, -2, -1]))    # Expected: -1  here o/p is not including circular
print(sol.maxSubarraySumCircular([8, -1, -3, 9, 5, -2, 6]))  # Expected: 28 here o/p is  including circular..only -3 is excluded

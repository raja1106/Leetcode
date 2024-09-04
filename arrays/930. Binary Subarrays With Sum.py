class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum_map = Counter()
        prefix_sum_map[0] = 1
        prefix_sum = 0
        count = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - goal in prefix_sum_map:
                count += prefix_sum_map[prefix_sum - goal]
            prefix_sum_map[prefix_sum] += 1

        return count

class Solution_sliding_window:
    # Helper function to count the number of subarrays with sum at most the given goal
    def sliding_window_at_most(self, nums: List[int], goal: int) -> int:
        start, current_sum, total_count = 0, 0, 0

        # Iterate through the array using a sliding window approach
        for end in range(len(nums)):
            current_sum += nums[end]

            # Adjust the window by moving the start pointer to the right
            # until the sum becomes less than or equal to the goal
            while start <= end and current_sum > goal:
                current_sum -= nums[start]
                start += 1

            # Update the total count by adding the length of the current subarray
            total_count += end - start + 1

        return total_count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.sliding_window_at_most(nums, goal) - self.sliding_window_at_most(nums, goal - 1)
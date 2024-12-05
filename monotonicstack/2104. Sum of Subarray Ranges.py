class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        # Nearest smaller element to the left for minimum contribution
        left_min = [-1] * n  # Index of the nearest smaller element to the left
        stack = []
        for i in range(n):
            # Maintain a monotonic increasing stack (for minimums)
            while stack and nums[stack[-1]] > nums[i]:  # Strictly smaller
                stack.pop()
            left_min[i] = stack[-1] if stack else -1  # If empty, no smaller element
            stack.append(i)

        # Nearest smaller element to the right for minimum contribution
        right_min = [n] * n  # Index of the nearest smaller element to the right
        stack = []
        for i in range(n - 1, -1, -1):
            # Maintain a monotonic increasing stack (for minimums)
            while stack and nums[stack[-1]] >= nums[i]:  # Allow equality to extend ranges
                stack.pop()
            right_min[i] = stack[-1] if stack else n  # If empty, no smaller element
            stack.append(i)

        # Nearest larger element to the left for maximum contribution
        left_max = [-1] * n  # Index of the nearest larger element to the left
        stack = []
        for i in range(n):
            # Maintain a monotonic decreasing stack (for maximums)
            while stack and nums[stack[-1]] < nums[i]:  # Strictly larger
                stack.pop()
            left_max[i] = stack[-1] if stack else -1  # If empty, no larger element
            stack.append(i)

        # Nearest larger element to the right for maximum contribution
        right_max = [n] * n  # Index of the nearest larger element to the right
        stack = []
        for i in range(n - 1, -1, -1):
            # Maintain a monotonic decreasing stack (for maximums)
            while stack and nums[stack[-1]] <= nums[i]:  # Allow equality to extend ranges
                stack.pop()
            right_max[i] = stack[-1] if stack else n  # If empty, no larger element
            stack.append(i)

        # Calculate the total contribution of each element
        total = 0
        for i in range(n):
            # Contribution of nums[i] as the maximum in subarrays
            max_contribution = nums[i] * (i - left_max[i]) * (right_max[i] - i)
            # Contribution of nums[i] as the minimum in subarrays
            min_contribution = nums[i] * (i - left_min[i]) * (right_min[i] - i)
            # Add the difference of max and min contributions
            total += (max_contribution - min_contribution)

        return total

from typing import List

class Solution:
    def findMSIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [nums[i] for i in range(n)]  # Initialize dp array with nums values directly
        max_sum = dp[0]  # Start max_sum with the first element in nums

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], nums[i] + dp[j])
            max_sum = max(max_sum, dp[i])

        return max_sum

# Example test case
solution = Solution()
print(solution.findMSIS([4, 1, 2, 6, 10, 1, 12]))  # Expected output should be the maximum sum
print(solution.findMSIS([3, 4, 5, 10]))           # Additional test case
print(solution.findMSIS([10, 5, 4, 3]))           # Descending test case

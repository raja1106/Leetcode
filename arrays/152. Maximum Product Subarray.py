from typing import List

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Finds the maximum product subarray in O(N) time.

        Example:
        nums = [-2,3,-4,-10]
        Expected Output: 120
        """
        n = len(nums)
        if n == 0:
            return 0  # Edge case: empty array

        global_max_product = nums[0]
        current_max_product = nums[0]
        current_min_product = nums[0]  # Track min product for negative swaps

        for i in range(1, n):
            num = nums[i]

            # If the number is negative, swap max and min
            if num < 0:
                current_max_product, current_min_product = current_min_product, current_max_product

            # Update max and min product
            current_max_product = max(num, current_max_product * num)
            current_min_product = min(num, current_min_product * num)

            # Update global max
            global_max_product = max(global_max_product, current_max_product)

        return global_max_product


class Solution_Brute_Force:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Brute Force Approach: O(N^2)
        Finds the maximum product subarray by checking all subarrays.
        """
        n = len(nums)
        global_max_product = float('-inf')

        # Iterate over all possible subarrays
        for start in range(n):
            product = 1
            for end in range(start, n):
                product *= nums[end]  # Calculate the product of subarray
                global_max_product = max(global_max_product, product)

        return global_max_product

# Example Test Cases
sol = Solution()
print(sol.maxProduct([2, 3, -2, 4]))  # Expected: 6
print(sol.maxProduct([-2, 0, -1]))    # Expected: 0
print(sol.maxProduct([0, 2]))         # Expected: 2
print(sol.maxProduct([-2, 3, -4]))    # Expected: 24

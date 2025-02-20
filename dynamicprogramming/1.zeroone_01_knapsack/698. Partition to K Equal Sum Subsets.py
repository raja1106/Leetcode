from typing import List
from functools import lru_cache


class Solution_Using_Memo:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum, remain = divmod(sum(nums), k)
        if remain != 0:  # If sum is not divisible by k, partitioning is impossible
            return False

        target_sum = total_sum  # Each subset must sum to this value
        nums.sort(reverse=True)  # Sorting helps in optimizing the search
        n = len(nums)

        # If the largest number is greater than target_sum, partitioning is impossible
        if nums[0] > target_sum:
            return False

        # Bitmask for tracking which numbers are used
        used = 0

        # Memoization dictionary
        memo = {}

        def dfs(current_sum, subsets_remaining, used):
            """
            DFS with bitmask memoization to check if we can form `k` subsets of `target_sum`
            """
            if subsets_remaining == 0:  # If all subsets are correctly formed
                return True
            if current_sum == target_sum:  # If one subset is completed, start a new subset
                return dfs(0, subsets_remaining - 1, used)

            memo_key = (current_sum, subsets_remaining, used)
            if memo_key in memo:  # If already computed, return stored result
                return memo[memo_key]

            for j in range(n):  # Try placing each unused number
                if (used & (1 << j)) or current_sum + nums[j] > target_sum:
                    continue  # Skip if already used or sum exceeds target

                # Mark number as used and recurse
                if dfs(current_sum + nums[j], subsets_remaining, used | (1 << j)):
                    memo[memo_key] = True
                    return True

            memo[memo_key] = False
            return False

        return dfs(0, k, 0)  # Start with 0 sum, all `k` subsets to form, and nothing used

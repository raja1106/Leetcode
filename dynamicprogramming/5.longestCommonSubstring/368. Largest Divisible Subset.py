from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        memo = {}
        best_result = []

        def dfs(i, slate):
            nonlocal best_result
            key = (i, tuple(slate))

            if key in memo:
                return memo[key]

            if i == len(nums):
                if len(slate) > len(best_result):
                    best_result = slate[:]
                return len(slate)

            # Exclude current element
            exclude_len = dfs(i + 1, slate)

            # Include current element if divisible
            include_len = 0
            if not slate or nums[i] % slate[-1] == 0:
                slate.append(nums[i])
                include_len = dfs(i + 1, slate)
                slate.pop()

            memo[key] = max(include_len, exclude_len)
            return memo[key]

        dfs(0, [])
        return best_result

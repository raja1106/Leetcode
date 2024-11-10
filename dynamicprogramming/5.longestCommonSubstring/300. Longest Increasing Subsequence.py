from typing import List


class Solution_Bottom_Up_Approach:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n  # dp[i] stores the LIS ending at index i
        maxLength = 1

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
            maxLength = max(maxLength, dp[i])

        return maxLength


class Solution_Brute_Force_1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest_length = -1
        def dfs(i,slate):
            nonlocal longest_length
            if i == len(nums):
                if len(slate) > longest_length:
                    longest_length = len(slate)
                return
            #exclude
            dfs(i+1,slate)
            #include
            if (not slate) or (nums[i] > slate[-1]):
                slate.append(nums[i])
                dfs(i+1,slate)
                slate.pop()
        dfs(0,[])
        return longest_length

class Solution_Bruteforce_2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i,slate):
            key = (i,tuple(slate))
            if key in memo:
                return memo[key]
            if i == len(nums):
                return len(slate)
            #exclude
            exclude_ans = dfs(i+1,slate)
            include_ans = 1
            #include
            if (not slate) or (nums[i] > slate[-1]):
                slate.append(nums[i])
                include_ans = dfs(i+1,slate)
                slate.pop()
            memo[key] = max(include_ans,exclude_ans)
            return max(include_ans,exclude_ans)
        return dfs(0,[])
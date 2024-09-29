class Solution_DP_Approach: #T(n) = O(n^2)
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i):
                if nums[j] + j >= i:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n - 1] if dp[n - 1] != float('inf') else -1


class Solution_Greedy_Approach: #T(n) = O(n)
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        # Variable to track the farthest reachable index
        farthest = 0

        for i in range(1, n):
            # Only update dp[i] if i is reachable
            while farthest + nums[farthest] < i:
                farthest += 1
            if farthest < i:
                dp[i] = dp[farthest] + 1

        return dp[ n -1] if dp[ n -1] != float('inf') else -1

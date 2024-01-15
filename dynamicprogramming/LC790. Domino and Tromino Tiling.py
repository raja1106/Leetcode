class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        # base case
        dp = [0] * (n + 1)
        l = [0] * (n + 1)
        u = [0] * (n + 1)
        if (n == 1):
            return 1
        dp[1],l[1],u[1] = 1,1,1
        dp[2],l[2], u[2]  = 2,2,2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + l[i - 2] + u[i - 2]
            l[i] = dp[i - 1] + u[i - 1]
            u[i] = dp[i - 1] + l[i - 1]

        return dp[n] % MOD
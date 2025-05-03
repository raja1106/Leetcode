class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]


class Solution_1:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        dp = [-1] * (n + 1)
        first = 1
        second = 2
        for i in range(3, n + 1):
            temp = second
            second = first + second
            first = temp
        return second


class Solution_2:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        first, second = 1, 2
        for _ in range(3, n + 1):
            second, first = first + second, second

        return second


class Solution_3:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        first, second = 1, 2
        for _ in range(3, n + 1):
            first, second = second, first + second

        return second

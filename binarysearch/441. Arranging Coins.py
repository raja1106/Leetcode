class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 0
        end = n
        while start <= end:
            mid = start + (end-start)//2
            x = mid*(mid+1)//2
            if x == n:
                return mid
            elif x < n:
                start = mid+1
            else:
                end = mid-1
        return end

    def arrangeCoins_1(self, n: int) -> int:
        start = 0
        end = n
        while start <= end:
            mid = start + (end - start) // 2
            x = mid * (mid + 1) // 2
            if x <= n:
                start = mid + 1
            else:
                end = mid - 1
        return end


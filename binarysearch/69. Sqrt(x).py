class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x

        while start <= end:
            mid = start+(end-start)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                start = mid+1
            else:
                end = mid-1
        return end


class Solution_two_region:
    def mySqrt(self, x: int) -> int:
        """
        lllllllLRrrrrr
        """
        start = 1
        end = x

        while start <= end:
            mid = start + (end - start) // 2
            sqr_mid = mid * mid
            if sqr_mid <= x:  # left region
                start = mid + 1
            else:
                end = mid - 1

        return end
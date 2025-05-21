class Solution_May_2025:
    def isPerfectSquare(self, num: int) -> bool:
        """
        lllllllLMRrrrrr
        """
        start = 1
        end = num
        while start <= end:
            mid = start + (end - start) // 2
            sqr_mid = mid * mid
            if sqr_mid == num:
                return True
            elif sqr_mid < num:  # left region
                start = mid + 1
            else:
                end = mid - 1

        return False

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 0
        end = num

        while start <= end:
            mid = start + (end - start) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                start = mid + 1
            else:
                end = mid - 1
        return False
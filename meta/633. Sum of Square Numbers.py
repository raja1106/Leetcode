class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start = 0
        end = int(sqrt(c))

        while start <= end:
            if start ** 2 + end ** 2 == c:
                return True
            elif start ** 2 + end ** 2 < c:
                start += 1
            else:
                end -= 1

        return False
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        start = 1
        end = max(ribbons)
        """
        llllllllLRrrrrrr
        L --> you can cut into k pieces
        R --> you can not cut into k pieces
        return L that is end
        """
        if k > sum(ribbons):
            return 0
        if k == sum(ribbons):
            return 1
        def can_split(length):
            total = 0
            for ribbon in ribbons:
                total += ribbon//length
            return total >= k

        while start <= end:
            mid = start+(end-start)//2
            if can_split(mid):
                start = mid+1
            else:
                end = mid-1

        return end
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        finalbad=0
        while(left<right):
            mid= left + (right - left) //2
            response=isBadVersion(mid)
            if response is True:
                right=mid
                finalbad = mid
            else:
                left=mid+1
        return left
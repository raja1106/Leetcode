from typing import List


class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        start=0
        end=len(arr)-1
        result=-1
        while(start<=end):
            mid=start+(end-start)//2

            if arr[mid] == mid:
                result = mid
                end = mid - 1
            elif arr[mid] > mid:
                end=mid-1
            else:
                start=mid+1
        return result

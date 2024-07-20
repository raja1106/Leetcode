from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start,end =1,len(arr)-2

        while (start <=end):
            mid = start+(end-start)//2

            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid+1] > arr[mid]: #if mid is in Ascending zone
                start = mid+1
            else:  #if mid is in Descending zone
                end=mid-1
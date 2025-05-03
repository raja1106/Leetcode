from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
                0 2 5 7 8 9 6 4 3
                0 9 8 7 5 4 3 2 1
                lllllLMRrrrrrr
                left region --> incremental
                right region -> decremental
                need to return M
        """
        start,end =1,len(arr)-2

        while (start <=end):
            mid = start+(end-start)//2

            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid+1] > arr[mid]: #if mid is in Ascending zone
                start = mid+1
            else:  #if mid is in Descending zone
                end=mid-1


class Solution_two_regions:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        0 2 5 7 8 9 6 4 3
        0 9 8 7 5 4 3 2 1
        lllllLRrrrrrr
        left region --> incremental
        right region -> decremental
        need to return L
        """
        start = 1
        end = len(arr) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if (mid - 1) >= 0 and arr[mid] > arr[mid - 1]:
                start = mid + 1
            else:
                end = mid - 1

        return end

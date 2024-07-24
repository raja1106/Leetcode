class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get(arr, i):
            if i < 0:
                return float('-inf')
            elif i >= len(arr):
                return float('inf')
            else:
                return arr[i]
        m, n = len(nums1), len(nums2)
        if (m + n) % 2 == 1:
            k = (m + n) // 2 + 1
        else:
            k = (m + n) // 2

        start, end = 0,m-1

        while start <= end:
            mid = start + (end-start)//2
            if get(nums2,k-1-mid-1) <=get(nums1,mid) <=get(nums2,k-1-mid):
                kthsmallest = get(nums1,mid)
                succ = min(get(nums1,mid+1),get(nums2,k-1-mid))
                break
            elif get(nums1,mid) > get(nums2,k-1-mid):
                end = mid-1
            else:
                start = mid+1
        if start == end+1:
            kthsmallest = get(nums2,k-start-1)
            succ = min(get(nums1,start),get(nums2,k-start))
        if (m + n) % 2 == 1:
            return kthsmallest
        else:
            return (kthsmallest+succ)/2.0
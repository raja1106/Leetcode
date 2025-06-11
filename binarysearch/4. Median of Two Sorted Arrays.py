class Solution:
    #Function to find the median of two sorted arrays.
    def findMedianSortedArrays(self, arr1, arr2):
        len1, len2 = len(arr1), len(arr2)
        if len1 > len2:
            arr2, arr1 = arr1,arr2
        len1, len2 = len(arr1), len(arr2)
        total_length = len1 + len2
        left_partition_size = (len1 + len2 + 1) // 2
        low, high = 0, len1
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left_partition_size - mid1

            l1 = arr1[mid1 - 1] if mid1 > 0 else float('-inf')
            l2 = arr2[mid2 - 1] if mid2 > 0 else float('-inf')
            r1 = arr1[mid1] if mid1 < len1 else float('inf')
            r2 = arr2[mid2] if mid2 < len2 else float('inf')

            if l1 <= r2 and l2 <= r1:
                if total_length % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0

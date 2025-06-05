class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        start, end = 0, m

       # [11 12 17] [13 14 15 16]   m =3 n = 4, pX = 1   pY=4-1=3

        while start <= end:
            mid = start + (end - start) // 2
            partitionX = mid
            partitionY = (m + n + 1) // 2 - partitionX

            # Handle edge cases
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == m else nums1[partitionX]

            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == n else nums2[partitionY]

            if maxX <= minY and maxY <= minX:
                # We have found the correct partition
                if (m + n) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                else:
                    return max(maxX, maxY)

            elif maxX > minY:
                # Too far to the right, move left
                end = mid - 1
            else:
                # Too far to the left, move right
                start = mid + 1

        raise ValueError("Input arrays are not sorted or valid")

class Solution_Best_One:
    #Function to find the median of two sorted arrays.
    def findMedianSortedArrays(self, arr1, arr2):
        len1, len2 = len(arr1), len(arr2)

        if len1 > len2:
            return self.median(arr2, arr1)

        total_length = len1 + len2
        left_partition_size = (len1 + len2 + 1) // 2

        low, high = 0, len1
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left_partition_size - mid1

            l1 = arr1[mid1 - 1] if mid1 > 0 else float('-inf')
            r1 = arr1[mid1] if mid1 < len1 else float('inf')
            l2 = arr2[mid2 - 1] if mid2 > 0 else float('-inf')
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

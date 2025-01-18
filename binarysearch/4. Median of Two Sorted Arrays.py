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
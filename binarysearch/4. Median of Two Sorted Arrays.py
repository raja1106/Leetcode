class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Helper function to safely retrieve elements with boundary checks.
        # Returns -inf if index is out of bounds on the left (i < 0),
        # and +inf if index is out of bounds on the right (i >= len(arr)).
        def get(arr, i):
            if i < 0:
                return float('-inf')
            elif i >= len(arr):
                return float('inf')
            else:
                return arr[i]

        m, n = len(nums1), len(nums2)
        # Determine the value of k based on the total length of the arrays.
        # If the total length is odd, k represents the middle element.
        # If even, k represents the index of the element just before the midpoint.
        # For odd lengths, we add 1 to ensure k points to the exact median.
        if (m + n) % 2 == 1:
            k = (m + n) // 2 + 1
        else:
            k = (m + n) // 2

        start, end = 0, m - 1

        # Perform binary search to locate the k-th smallest element.
        # This efficiently narrows down the search by comparing the current mid element
        # in nums1 with potential candidates in nums2.
        while start <= end:
            mid = start + (end - start) // 2
            # Check if nums1[mid] is the k-th smallest element by ensuring it falls
            # between the appropriate values in nums2.
            if get(nums2, k - 1 - mid - 1) <= get(nums1, mid) <= get(nums2, k - 1 - mid):
                kthsmallest = get(nums1, mid)
                # Identify the successor to calculate median for even-length arrays.
                succ = min(get(nums1, mid + 1), get(nums2, k - 1 - mid))
                break
            # If nums1[mid] is too large, adjust the search range to the left.
            elif get(nums1, mid) > get(nums2, k - 1 - mid):
                end = mid - 1
            # If nums1[mid] is too small, adjust the search range to the right.
            else:
                start = mid + 1

        # If the binary search exits without finding a match, the k-th element
        # resides in nums2.
        if start == end + 1:
            kthsmallest = get(nums2, k - start - 1)
            succ = min(get(nums1, start), get(nums2, k - start))

        # Return the median based on whether the total length is odd or even.
        if (m + n) % 2 == 1:
            return kthsmallest
        else:
            return (kthsmallest + succ) / 2.0



class Solution_GPT:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)

        start, end = 0, x

        while start <= end:
            partitionX = (start + end) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            # Handle edge cases
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == x else nums1[partitionX]

            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == y else nums2[partitionY]

            if maxX <= minY and maxY <= minX:
                # We have found the correct partition
                if (x + y) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                else:
                    return max(maxX, maxY)

            elif maxX > minY:
                # We are too far on the right side for partitionX, move left
                end = partitionX - 1
            else:
                # We are too far on the left side for partitionX, move right
                start = partitionX + 1

        raise ValueError("Input arrays are not sorted or valid")

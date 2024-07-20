class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # If the first element is larger than k, the k-th positive missing number would be k
        if arr[0] > k:
            return k

        # Use binary search to find k-th positive missing number
        start, end = 0, len(arr)-1
        while start <= end:
            mid = start+(end - start) // 2  # Use integer division for Python 3

            # Calculate the number of negative elements up to index mid
            missing_until_mid = arr[mid] - (mid + 1)

            # If the number of missing elements is greater or equals k, look in the left half
            if missing_until_mid >= k:
                end = mid-1
            else:
                start = mid + 1  # Otherwise, look in the right half

        missingonleft = arr[end] - (end+1)
        return arr[end] + (k - missingonleft)

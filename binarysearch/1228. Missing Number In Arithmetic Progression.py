class Solution:
    def missingNumber(self, arr: List[int]) -> int:

        d = (arr[-1]-arr[0])//len(arr)

        start =0
        end = len(arr)-1

        while start <= end:
            mid = start + (end-start)//2

            if arr[mid] == arr[0]+ (mid*d):
                start = mid+1
            else:
                end = mid-1

        return arr[end]+d
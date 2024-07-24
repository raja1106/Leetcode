class Solution:


    def splitArray_I(self, nums: List[int], m: int) -> int:

        start, end = max(nums), sum(nums)

        while start <= end:
            mid = start + ((end - start) // 2) # here mid is largest sum possible
            sub_arrays = 1
            total = 0
            for i in range(len(nums)):
                total += nums[i]
                if total > mid:
                    total = nums[i]
                    sub_arrays += 1
            if sub_arrays > m:
                start = mid + 1
            else:
                end = mid - 1
        return start
    def splitArray(self, nums: List[int], m: int) -> int:
        def canSplit(largest):
            subarray = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    curSum = n
            return subarray + 1 <= m

        start, end = max(nums), sum(nums)
        while start <= end:
            mid = start + ((end - start) // 2)
            if canSplit(mid):
                end = mid - 1
            else:
                start = mid + 1
        return start




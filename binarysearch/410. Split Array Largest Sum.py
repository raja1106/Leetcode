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

    class Solution_Using_DP:
        def splitArray(self, nums: List[int], m: int) -> int:
            dp = {}

            def dfs(i, m):
                if m == 1:
                    return sum(nums[i:])
                if (i, m) in dp:
                    return dp[(i, m)]

                result, curSum = float("inf"), 0
                for j in range(i, len(nums) - m + 1):
                    curSum += nums[j]
                    maxSum = max(curSum, dfs(j + 1, m - 1))
                    result = min(result, maxSum)
                    if curSum > result:
                        break
                dp[(i, m)] = result
                return result

            return dfs(0, m)





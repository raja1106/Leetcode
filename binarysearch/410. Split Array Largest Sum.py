class Solution_Best:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        Split nums into k non-empty subarrays such that the
        largest subarray sum is minimized.

        Example:
        nums = [7,2,5,10,8], k = 2

        Possible splits:
        [7]        [2,5,10,8] -> largest sum = 25
        [7,2]      [5,10,8]   -> largest sum = 23
        [7,2,5]    [10,8]     -> largest sum = 18
        [7,2,5,10] [8]        -> largest sum = 24

        Minimum answer = max(nums)
        Maximum answer = sum(nums)

        For a candidate largest sum `max_allowed_sum`:
        - if we can split into <= k parts, it is feasible
        - if we need > k parts, it is not feasible
         This feasibility is monotonic, so we use binary search.

        llllllLRrrrrr
        left side >k
        right_side <=k

        The idea is correct, but it should say:

        smaller allowed sum => need more subarrays
        larger allowed sum => need fewer subarrays
        More precisely:
        left side: requires > k subarrays → invalid
        right side: requires <= k subarrays → valid
        That is the monotonic property that makes binary search work.
        """

        def is_feasible(max_allowed_sum: int) -> bool:
            subarray_count = 1
            current_subarray_sum = 0

            for num in nums:
                if current_subarray_sum + num > max_allowed_sum:
                    subarray_count += 1
                    current_subarray_sum = 0

                current_subarray_sum += num

                if subarray_count > k:
                    return False

            return True

        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = left + (right - left) // 2

            if is_feasible(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

class Solution_Using_TopDown:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        memo = {}

        def dfs(i, m):
            # If we consumed all nums, valid only if m == 0
            if i == n:
                return 0 if m == 0 else float("inf")

            # If we still need to create subarrays but no elements left
            if m == 0:
                return float("inf")

            # Check memo
            if (i, m) in memo:
                return memo[(i, m)]

            res = float("inf")
            curSum = 0

            # Try every possible end point j for the current subarray
            for j in range(i, n - m + 1):
                curSum += nums[j]
                res = min(res, max(curSum, dfs(j + 1, m - 1)))

            memo[(i, m)] = res
            return res

        return dfs(0, k)


class Solution_Bruteforce:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        nums = [7,2,5,10,8], k = 2 --> n-k index
        7 2 5 10   8
        """
        global_min = float('inf')

        # r --> subarrays remaining
        def helper(i, r, path):
            nonlocal global_min
            if r == 1:
                current_subarray_sum = sum(nums[i:])
                path.append(current_subarray_sum)  # path : list of sub arrays (list of list elements)
                local_max = max(path)
                global_min = min(global_min, local_max)
                path.pop()
                return

            for start in range(i, len(nums) - k + 1):
                path.append(sum(nums[i:start + 1]))
                helper(start + 1, r - 1, path)
                path.pop()
            return

        helper(0, k, [])
        return global_min






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





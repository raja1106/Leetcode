from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]

            # don't include the current job
            res = dfs(i + 1)

            # include the current job
            j = i + 1
            while j < len(intervals):
                if intervals[i][1] <= intervals[j][0]:
                    break
                j += 1

            cache[i] = res = max(res, intervals[i][2] + dfs(j))
            return res

        return dfs(0)

from typing import List
from bisect import bisect_left

class Solution_Using_Binary_Search:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Sort jobs by start time
        jobs = sorted(zip(startTime, endTime, profit))
        starts = [s for s, _, _ in jobs]   # Extract sorted start times for binary search
        memo = {}

        def dfs(i: int) -> int:
            # Base case: no more jobs
            if i == len(jobs):
                return 0
            if i in memo:
                return memo[i]

            # Option 1: skip the current job
            max_profit = dfs(i + 1)

            # Option 2: include the current job
            # Find the next job that starts after the current job's end time
            next_index = bisect_left(starts, jobs[i][1])
            max_profit = max(max_profit, jobs[i][2] + dfs(next_index))

            memo[i] = max_profit
            return max_profit

        return dfs(0)

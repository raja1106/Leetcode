from collections import deque
from typing import List


class Solution_BFS:
    def jump(self, nums: List[int]) -> int:
        q = deque([(0, 0)])
        visited = set([0])
        target = len(nums) - 1

        while q:
            node_index, steps = q.popleft()

            if node_index == target:
                return steps

            max_index = node_index + nums[node_index]

            for i in range(node_index + 1, max_index + 1):
                if i == target:
                    return steps + 1
                if (i < target) and (not i in visited):
                    visited.add(i)
                    q.append((i, steps + 1))

        return 0


class Solution_DFS:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i == len(nums) - 1:
                return 0

            if i >= len(nums):
                return float('inf')

            min_steps = float('inf')

            # FIX: start from 1, not 0
            for j in range(1, nums[i] + 1):
                current_steps = 1 + dfs(i + j)
                min_steps = min(min_steps, current_steps)

            memo[i] = min_steps
            return min_steps

        return dfs(0)

class Solution_DP_Approach: #T(n) = O(n^2)
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i):
                if nums[j] + j >= i:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n - 1] if dp[n - 1] != float('inf') else -1


class Solution_Greedy_Approach: #T(n) = O(n)
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        # Variable to track the farthest reachable index
        farthest = 0

        for i in range(1, n):
            # Only update dp[i] if i is reachable
            while farthest + nums[farthest] < i:
                farthest += 1
            if farthest < i:
                dp[i] = dp[farthest] + 1

        return dp[ n -1] if dp[ n -1] != float('inf') else -1

from typing import List, Optional

from typing import List

class Solution_Optimized:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        st = []
        n = len(nums)

        for i in range(n):
            # While:
            # 1) we have something to pop
            # 2) current value is smaller (better lexicographically)
            # 3) after popping, we can still build a length-k subsequence
            while st and st[-1] > nums[i] and (len(st) - 1 + (n - i)) >= k:
                st.pop()

            # keep pushing while we still need elements
            if len(st) < k:
                st.append(nums[i])

        return st

class Solution_Brute_Force:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        best: Optional[List[int]] = None

        def is_better(a: List[int], b: List[int]) -> bool:
            """True if a is lexicographically smaller than b (same length)."""
            for x, y in zip(a, b):
                if x != y:
                    return x < y
            return False  # equal => not better

        def dfs(i: int, chosen: List[int]) -> None:
            nonlocal best

            # If chosen length == k, evaluate
            if len(chosen) == k:
                if best is None or is_better(chosen, best):
                    best = chosen[:]  # copy
                return

            # If out of bounds, stop
            if i == n:
                return

            # Prune: not enough elements left to reach k
            if len(chosen) + (n - i) < k:
                return

            # Option 1: take nums[i]
            chosen.append(nums[i])
            dfs(i + 1, chosen)
            chosen.pop()

            # Option 2: skip nums[i]
            dfs(i + 1, chosen)

        dfs(0, [])
        return best if best is not None else []

from typing import List, Tuple
from functools import lru_cache

class Solution_Top_Down:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        INF = 10**18  # sentinel larger than any nums[i]

        @lru_cache(None)
        def dp(i: int, need: int) -> Tuple[int, ...]:
            """
            Best (lexicographically smallest) subsequence of length `need` from nums[i:].
            Returns a tuple.
            """
            if need == 0:
                return ()
            if i == n:
                return (INF,)  # impossible
            if n - i < need:
                return (INF,)  # impossible

            # Option 1: take nums[i]
            take = (nums[i],) + dp(i + 1, need - 1)

            # Option 2: skip nums[i]
            skip = dp(i + 1, need)

            # Choose lexicographically smaller valid tuple
            return take if take < skip else skip

        ans = dp(0, k)

        # If inputs are valid, ans won't start with INF
        if ans and ans[0] == INF:
            return []
        return list(ans)

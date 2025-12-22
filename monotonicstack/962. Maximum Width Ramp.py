from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        st = []  # stack of indices, nums values strictly decreasing

        # 1) Build decreasing stack of candidate left indices
        for i in range(n):
            if not st or nums[i] < nums[st[-1]]:
                st.append(i)

        # 2) Scan from right to left and expand ramps
        max_width = 0
        for j in range(n - 1, -1, -1):
            while st and nums[j] >= nums[st[-1]]:
                i = st.pop()
                max_width = max(max_width, j - i)
            if not st:  # early exit: no more left candidates
                break

        return max_width


class Solution_Bruteforce:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_width = 0
        n = len(nums)
        for i in range(n):
            local_max_width = 0
            for j in range(n):
                if nums[j] >= nums[i]:
                    local_max_width = max(local_max_width, j - i)

            max_width = max(local_max_width, max_width)
        return max_width
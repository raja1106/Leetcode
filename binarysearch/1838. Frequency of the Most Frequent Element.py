from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        # prefix[i] = sum of nums[0 .. i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        def window_cost(l, r):
            """Cost to make [l..r] all equal to nums[r]."""
            window_sum = prefix[r+1] - prefix[l]
            window_size = r - l + 1
            return nums[r] * window_size - window_sum

        max_freq = 1

        # For each r, binary search the smallest l using template
        for r in range(n):

            start = 0
            end = r
            best_l = r     # worst case: only the element itself

            # Template binary search:
            #   valid(mid) = (cost(mid, r) <= k)
            #   want leftmost mid that is valid
            while start <= end:
                mid = start + (end - start)//2

                if window_cost(mid, r) <= k:
                    # mid is in RIGHT region of valid answers (valid → try to extend left)
                    best_l = mid
                    end = mid - 1
                else:
                    # mid is in LEFT invalid region (invalid → move right)
                    start = mid + 1

            max_freq = max(max_freq, r - best_l + 1)

        return max_freq

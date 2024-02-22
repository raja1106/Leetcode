from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        window_zero=0
        global_ans=-1

        for i in range(len(nums)):
            if nums[i] == 0:
                window_zero += 1

            while left <= i and window_zero >k:
                if nums[left] == 0:
                    window_zero -= 1
                left += 1
            global_ans = max(global_ans,i-left+1)

        return global_ans
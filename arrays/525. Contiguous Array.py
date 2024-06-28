from typing import List


class Solution:  # 1,1,0,0,1,1 --> 4--> 6-2
    def findMaxLength(self, nums: List[int]) -> int:
        balance_map = {0: 0}
        global_max = 0
        balance = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                balance += 1
            else:
                balance -= 1
            if balance in balance_map:
                global_max = max(global_max, (i + 1) - balance_map[balance])
            if balance not in balance_map:
                balance_map[balance] = i + 1
        return global_max

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

class Solution1:
    def findMaxLength(self, nums: List[int]) -> int:
        balance_map = {0: -1}  # Initialize with -1 to handle subarray starting from index 0
        global_max = 0
        balance = 0

        for i in range(len(nums)):
            # Update balance based on current value
            if nums[i] == 1:
                balance += 1
            else:
                balance -= 1

            # Check if the current balance has been seen before
            if balance in balance_map:
                # Calculate the subarray length
                global_max = max(global_max, i - balance_map[balance])
            else:
                # Store the first occurrence of this balance
                balance_map[balance] = i

        return global_max

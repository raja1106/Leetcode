from typing import List


class Solution:  # 1,1,0,0,1,1 --> 4--> 6-2
    def findMaxLength(self, nums: List[int]) -> int:
        balance_map = {0: 0} #here we are storing length of subarray
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
                balance_map[balance] = i + 1 #here we are storing length of subarray
        return global_max

class Solution1:
    def findMaxLength(self, nums: List[int]) -> int:
        balance_map = {0: -1}  #here we are storing at which index the subarray is ending
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
                balance_map[balance] = i #here we are storing at which index the subarray is ending

        return global_max


class Solution_Bruteforce:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        [1,1,0,0,0,0,1,1,1,1]

        """

        zero_count = one_count = 0
        max_length = 0
        for j in range(len(nums)):
            zero_count = one_count = 0
            for i in range(j, len(nums)):
                if nums[i] == 0:
                    zero_count += 1
                elif nums[i] == 1:
                    one_count += 1
                if zero_count == one_count:
                    max_length = max(max_length, i - j + 1)

        return max_length





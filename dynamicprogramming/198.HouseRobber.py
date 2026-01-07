from typing import List


class Solution_Top_down_way:
    def rob(self, nums: List[int]) -> int:
        house_values = nums
        max_loot_from_index = {}

        def max_loot(start_index: int) -> int:
            if start_index in max_loot_from_index:
                return max_loot_from_index[start_index]

            if start_index >= len(house_values):
                return 0

            # Option 1: Skip current house
            skip_current = max_loot(start_index + 1)

            # Option 2: Rob current house
            rob_current = house_values[start_index] + max_loot(start_index + 2)

            max_loot_from_index[start_index] = max(skip_current, rob_current)
            return max_loot_from_index[start_index]

        loot_starting_from_first = max_loot(0)
        loot_starting_from_second = max_loot(1)

        return max(loot_starting_from_first, loot_starting_from_second)

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp =[0]*len(nums)
        dp[0]=nums[0]

        if(len(nums)>1):
            dp[1]=max(nums[0],nums[1])
        if (len(nums) > 2):
            dp[2] = max(nums[0]+nums[2], nums[1])

        for i in range (3,len(nums)):
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
            # nums[i]+dp[i-2]  -->  This is include option of nums[i]
            # dp[i-1]  -->  This is exclude option of nums[i]
        return dp[-1]

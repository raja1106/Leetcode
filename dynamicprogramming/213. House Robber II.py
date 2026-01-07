from typing import List

class Solution_top_down_way:
    def rob(self, house_values: List[int]) -> int:
        if len(house_values) == 1:
            return house_values[0]
        if len(house_values) == 2:
            return max(house_values[0], house_values[1])

        max_loot_memo = {}

        def max_loot(current_index: int, first_house_taken: bool) -> int:
            if (current_index, first_house_taken) in max_loot_memo:
                return max_loot_memo[(current_index, first_house_taken)]

            if current_index >= len(house_values):
                return 0

            # If first house was taken, last house cannot be robbed
            if first_house_taken and current_index == len(house_values) - 1:
                return 0

            # Option 1: Skip current house
            skip_current = max_loot(current_index + 1, first_house_taken)

            # Option 2: Rob current house
            rob_current = house_values[current_index] + \
                          max_loot(current_index + 2, first_house_taken)

            max_loot_memo[(current_index, first_house_taken)] = max(skip_current, rob_current)
            return max_loot_memo[(current_index, first_house_taken)]

        # Case 1: Rob first house → cannot rob last house
        loot_with_first_house = max_loot(0, True)

        # Case 2: Skip first house → last house allowed
        loot_without_first_house = max_loot(1, False)

        return max(loot_with_first_house, loot_without_first_house)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        if(len(nums)==2):
            return max(nums[0],nums[1])
        if(len(nums)==3):
            return max(nums[0],nums[2],nums[1])
        dp1= [0] * (len(nums) - 1)
        dp2= [0] * (len(nums))
        dp1[0]=nums[0]
        dp1[1]=max(nums[0],nums[1])
        if(len(nums)==1):
            return max(nums[0],nums[1])
        for i in range(2,len(nums) - 1):
            dp1[i]=max(dp1[i-1],dp1[i-2]+nums[i])
        dp2[0] =0
        dp2[1]=nums[1]
        dp2[2]=max(nums[2],nums[1])
        for i in range(3,len(nums)):
            dp2[i]=max(dp2[i-1],dp2[i-2]+nums[i])
        return max(dp1[-1],dp2[-1])

class Solution1:#TODO Need to uderstand below solution better
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        def max_money(nums):
            nums = [0]+nums
            for i in range(3,len(nums)):
                nums[i]+=max(nums[i-3],nums[i-2])
            return max(nums[-1],nums[-2])
        return max(max_money(nums[1:]),max_money(nums[:-1])) if len(nums) > 2 else max(nums)
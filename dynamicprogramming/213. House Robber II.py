from typing import List
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
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_map = {}

        for i in range(len(nums)):
            if (target-nums[i]) in index_map:
                return i,index_map[target-nums[i]]
            else:
                index_map[nums[i]] =i



obj=Solution()
print(obj.twoSum([3,2,4],11))
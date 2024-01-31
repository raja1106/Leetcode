from typing import List

#  4,2,3,7,8,2,3,1 --> 1,2,3,4,5,6,7,8 --> 2, 3, 1--> 3,2,1-->1,2,3
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            while i != nums[i]-1:
                d=nums[i]-1
                if nums[d] != nums[i]:
                    nums[d],nums[i] = nums[i],nums[d]
                else:
                    break
        for i in range(len(nums)):
            if(i+1 != nums[i]):
                result.append(i+1)

        return result
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


class Solution_gpt:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            # target_index = nums[i] -1
            while nums[i] - 1 < n and nums[i] - 1 != i:
                target_index = nums[i] - 1
                if nums[i] == nums[target_index]:
                    break
                nums[i], nums[target_index] = nums[target_index], nums[i]

        result = []
        for i in range(n):
            if i != nums[i] - 1:
                result.append(i + 1)

        return result


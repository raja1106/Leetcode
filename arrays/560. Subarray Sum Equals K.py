from typing import List

#2,5,5,0,2   k=7
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap={}
        hmap[0]=1
        prefixSum=0
        globalCount=0
        for i in range(len(nums)):
            prefixSum +=nums[i]
            if prefixSum-k in hmap:
                globalCount +=hmap[prefixSum-k]

            if prefixSum in hmap:
                hmap[prefixSum] +=1
            else:
                hmap[prefixSum]=1
        
        return globalCount
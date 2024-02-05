from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hmap={}
        hmap[0]=1
        prefixsum=0
        global_count=0
        for i in range(len(nums)):
            prefixsum = (prefixsum+nums[i])%k
            if prefixsum in hmap:
                global_count +=hmap[prefixsum]
            if prefixsum in hmap:
                hmap[prefixsum] +=1
            else:
                hmap[prefixsum] = 1
        return global_count
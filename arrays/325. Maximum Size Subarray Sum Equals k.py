import sys
from typing import List
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        hmap={}
        hmap[0]=0
        prefixsum=0
        maxv=0
        for i in range(len(nums)):
            prefixsum=prefixsum+nums[i]
            if prefixsum-k in hmap:
                maxv=max(maxv,i+1-hmap[prefixsum-k])
            if  prefixsum not in hmap:
                hmap[prefixsum]=i

        return maxv
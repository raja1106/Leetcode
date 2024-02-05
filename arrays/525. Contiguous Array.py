from typing import List
class Solution: #1,1,0,0,1,1 --> 4--> 6-2
    def findMaxLength(self, nums: List[int]) -> int:
        hmap={}
        hmap[0]=0
        global_max=0
        prefixexcess=0
        for i in range(len(nums)):
            if nums[i]==1:
                prefixexcess+=1
            else:
                prefixexcess-=1
            if prefixexcess in hmap:
                global_max=max(global_max,(i+1)-hmap[prefixexcess])
            if  prefixexcess not in hmap:
                hmap[prefixexcess]=i+1
        return global_max
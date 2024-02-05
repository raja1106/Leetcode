from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        hmap={}
        hmap[0]=1
        hmap[1]=0
        prefixsum=0
        total=0
        for i in range(len(arr)):
            prefixsum = arr[i]+prefixsum
            if prefixsum%2==0:
                total += hmap[1]
                hmap[0]=hmap[0]+1
            else:
                total+=hmap[0]
                hmap[1] = hmap[1] + 1

        return total
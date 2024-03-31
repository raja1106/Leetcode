import collections
from typing import List
from collections import deque


#TODOO: Need to try with Segment Tree as this solution using Deque doesn't work for all input
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        dq = collections.deque()
        result=[]
        for i in range(len(nums)-1,-1,-1):
            while dq and dq[-1] > nums[i]:
                dq.pop()
            dq.append(nums[i])
            if i <len(nums)-1 and nums[i] == nums[i+1]:
                result.append(result[-1])
            else:
                result.append(len(dq) - 1)
        result.reverse()
        return result


    def countSmaller(self, nums: List[int]) -> List[int]:

        q=deque()
        result= []
        for i in range(len(nums)-1,-1,-1):
            while q and q[-1] >= nums[i]:
                q.pop()
            q.append(nums[i])
            result.append(len(q)-1)

        result.reverse()
        return result


obj =Solution()
obj.countSmaller([-1,-1])

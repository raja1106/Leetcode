import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        d = collections.deque()
        def pushin(val):
            while d and d[-1]<val:
                d.pop()
            d.append(val)

        for i in range(k):
            pushin(nums[i])

        result=[d[0]]

        for i in range(k,len(nums)):
            if nums[i-k] == d[0]:
                d.popleft()
            pushin(nums[i])
            result.append(d[0])

        return result

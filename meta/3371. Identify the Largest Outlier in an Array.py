from collections import Counter
from typing import List

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total_sum = sum(nums) #20
        counts = Counter(nums)
        outlier = float('-inf')
        for num in nums:
            counts[num] -= 1
            total_sum -= num #10
            if total_sum % 2 == 0 and counts[total_sum // 2] > 0:
                outlier = max(outlier, num)
            # This line modifies the count of the last 'n' after the loop
            counts[num] += 1
            total_sum += num
        return outlier
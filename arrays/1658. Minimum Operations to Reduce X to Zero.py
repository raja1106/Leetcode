from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target=sum(nums)-x
        max_size=-1
        left=0
        window_sum=0

        for i in range(len(nums)):
            window_sum += nums[i]

            while left <= i and window_sum > target:
                window_sum -= nums[left]
                left += 1

            if (window_sum == target):
                max_size = max(max_size, i - left + 1)

        return -1 if max_size == -1 else len(nums)-max_size
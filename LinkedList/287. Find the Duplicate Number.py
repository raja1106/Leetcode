from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find the intersection point in the cycle.
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Phase 2: Find the entrance to the cycle.
        start = 0
        while slow != start:
            slow = nums[slow]
            start = nums[start]

        return slow
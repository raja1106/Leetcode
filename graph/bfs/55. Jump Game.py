from collections import deque
from typing import List

class Solution:#O(n^2)
    def canJump(self, nums: List[int]) -> bool:
        queue = deque([0])  # Tracks indices to process
        visited = {0}  # Tracks indices already visited
        target_index = len(nums) - 1  # Target index to reach

        while queue:
            current_index = queue.popleft()  # Process the current index

            # If we reach the target index, return True
            if current_index == target_index:
                return True

            # Calculate the farthest index we can jump to
            farthest_jump = current_index + nums[current_index]

            # Iterate through all reachable indices from the current index
            for next_index in range(current_index + 1, farthest_jump + 1):
                # If we reach the target index, return True
                if next_index == target_index:
                    return True
                # If the index is within bounds and not visited, enqueue it
                if next_index < target_index and next_index not in visited:
                    visited.add(next_index)
                    queue.append(next_index)

        return False


class Solution_Greedy: #O(n)
    def canJump(self, nums: List[int]) -> bool:
        """
        Determine if it's possible to reach the last index of `nums` given
        each element in `nums` indicates the maximum jump length from that position.

        :param nums: List[int] - array where nums[i] is the maximum jump length at index i
        :return: bool - True if we can reach the last index, otherwise False
        """

        # 'reachable' represents the farthest index we can reach so far.
        reachable = 0

        # Loop over each index in the array
        for i in range(len(nums)):
            # If the current index is beyond the farthest we've been able to reach,
            # it means we cannot get here, so we cannot move further from here.
            if i > reachable:
                return False

            # Update 'reachable' to be the maximum of itself and the new jump from index 'i'.
            # i + nums[i] is the farthest index we can jump to from the current position.
            reachable = max(reachable, i + nums[i])

            # If, at any point, the farthest reachable index is at or beyond the last index,
            # we conclude it's possible to reach the end of the array.
            if reachable >= len(nums) - 1:
                return True

        # If we've finished iterating and never reached or exceeded the last index, return False.
        return False

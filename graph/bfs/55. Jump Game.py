from collections import deque
from typing import List

class Solution:
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

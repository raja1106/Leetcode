from collections import deque
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize the queue with the starting index and step count
        queue = deque([(0, 0)])  # (current_index, steps_taken)
        visited_indices = {0}  # Track visited indices
        target_index = len(nums) - 1  # Target index to reach

        while queue:
            current_index, steps = queue.popleft()  # Dequeue the current index and step count

            # If we've reached the target index, return the steps
            if current_index == target_index:
                return steps

            # Calculate the farthest index we can jump to
            farthest_jump = current_index + nums[current_index]

            # Iterate through all reachable indices from the current index
            for next_index in range(current_index + 1, farthest_jump + 1):
                # If we can directly reach the target index, return steps + 1
                if next_index == target_index:
                    return steps + 1
                # If the index is within bounds and not visited, enqueue it
                if next_index < target_index and next_index not in visited_indices:
                    visited_indices.add(next_index)
                    queue.append((next_index, steps + 1))

        return 0  # If the loop finishes without reaching the target, return 0

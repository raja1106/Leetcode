from collections import deque


class Solution_Greedy:
    def minimumSteps(self, s: str) -> int:
        # We use a greedy approach: every '0' must move past all '1's
        # currently to its left.
        total_swaps = 0
        ones_encountered = 0

        for char in s:
            if char == '1':
                ones_encountered += 1
            else:
                # This '0' needs to jump over every '1' seen so far
                total_swaps += ones_encountered

        return total_swaps



class Solution_UsingQueue:
    def minimumSteps(self, s: str) -> int:
        zero_indices = deque()

        # Collect all positions of zeros
        for i, char in enumerate(s):
            if char == '0':
                zero_indices.append(i)

        total_swaps = 0
        target_index = 0

        # Move each zero to the next available leftmost slot
        while zero_indices:
            current_index = zero_indices.popleft()
            total_swaps += (current_index - target_index)
            target_index += 1

        return total_swaps

class Solution_bruteForce:
    def minimumSteps(self, s: str) -> int:
        # Convert to list because strings in Python are immutable
        chars = list(s)
        total_swaps = 0
        swapped = True

        # Keep scanning until we make a full pass with no swaps
        while swapped:
            swapped = False
            for i in range(len(chars) - 1):
                # If we find a '1' followed by a '0', swap them
                if chars[i] == '1' and chars[i + 1] == '0':
                    chars[i], chars[i + 1] = chars[i + 1], chars[i]
                    total_swaps += 1
                    swapped = True

        return total_swaps
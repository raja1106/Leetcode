class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        i, j = 0, 0

        while i < n or j < n:
            # Skip underscores in start
            while i < n and start[i] == '_':
                i += 1

            # Skip underscores in target
            while j < n and target[j] == '_':
                j += 1

            # If both reach end, valid
            if i == n and j == n:
                return True

            # If only one reaches end, invalid (count mismatch)
            if i == n or j == n:
                return False

            # Check 1: Characters must match (Relative Order Invariant)
            if start[i] != target[j]:
                return False

            # Check 2: Directional Constraints
            # 'L' can only move left (start_index >= target_index)
            if start[i] == 'L' and i < j:
                return False

            # 'R' can only move right (start_index <= target_index)
            if start[i] == 'R' and i > j:
                return False

            i += 1
            j += 1

        return True
from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Automatically create sets when accessing a new key
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)  # Key: (row // 3, col // 3) as a tuple

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue

                # Box index as a tuple (3x3 grid)
                box_id = (r // 3, c // 3)

                # If the value is already present, it's invalid
                if val in rows[r] or val in cols[c] or val in boxes[box_id]:
                    return False

                # Otherwise, add the value to the corresponding sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_id].add(val)

        return True

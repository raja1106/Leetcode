from typing import List
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Modify board in-place to solve the Sudoku.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)  # Key: (r//3, c//3)

        # Step 1: Fill initial state
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3, c // 3)].add(val)

        def backtrack(r: int, c: int) -> bool:
            # Move to next row if end of column is reached
            if c == 9:
                return backtrack(r + 1, 0)
            # End of board => success
            if r == 9:
                return True
            # Skip filled cells
            if board[r][c] != '.':
                return backtrack(r, c + 1)
            for d in map(str, range(1, 10)):
                box_id = (r // 3, c // 3)
                if d in rows[r] or d in cols[c] or d in boxes[box_id]:
                    continue
                # Place digit
                board[r][c] = d
                rows[r].add(d)
                cols[c].add(d)
                boxes[box_id].add(d)
                # Recurse
                if backtrack(r, c + 1):
                    return True
                # Backtrack
                board[r][c] = '.'
                rows[r].remove(d)
                cols[c].remove(d)
                boxes[box_id].remove(d)

            return False

        backtrack(0, 0)

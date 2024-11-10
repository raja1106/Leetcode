from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        num_rows, num_cols = len(mat), len(mat[0])
        result = []
        direction = 1  # 1 for up-right, -1 for down-left
        row, col = 0, 0

        while len(result) < num_rows * num_cols:
            result.append(mat[row][col])
            if direction == 1:  # Moving up-right
                if col == num_cols - 1:  # Hit the right border
                    row += 1
                    direction = -1
                elif row == 0:  # Hit the top border
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1
            else:  # Moving down-left
                if row == num_rows - 1:  # Hit the bottom border
                    col += 1
                    direction = 1
                elif col == 0:  # Hit the left border
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1

        return result

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for r in zero_rows:
            for j in range(n):
                matrix[r][j] = 0

        for c in zero_cols:
            for i in range(m):
                matrix[i][c] = 0
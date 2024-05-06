from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        square_matrix = [[0 for _ in range(n)] for _ in range(m)]

        global_max = 0

        for col in range(n):
            if matrix[0][col] == '1':
                square_matrix[0][col] = 1
                global_max = 1

        for row in range(m):
            if matrix[row][0] == '1':
                square_matrix[row][0] = 1
                global_max = 1

        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == '0':
                    square_matrix[row][col] = 0
                else:
                    square_matrix[row][col] = 1 + (
                        min(square_matrix[row][col - 1], square_matrix[row - 1][col], square_matrix[row - 1][col - 1]))
                global_max = max(global_max, square_matrix[row][col])

        return global_max * global_max





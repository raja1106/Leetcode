from typing import List

from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            self.prefixsum = []
            return

        m = len(matrix)
        n = len(matrix[0])

        # Initialize the prefix sum matrix
        prefixsum = [[0 for _ in range(n)] for _ in range(m)]
        prefixsum[0][0] = matrix[0][0]

        # Fill the first row
        for col in range(1, n):
            prefixsum[0][col] = prefixsum[0][col-1] + matrix[0][col]

        # Fill the first column
        for row in range(1, m):
            prefixsum[row][0] = prefixsum[row-1][0] + matrix[row][0]

        # Fill the rest of the prefix sum matrix
        for row in range(1, m):
            for col in range(1, n):
                prefixsum[row][col] = (prefixsum[row-1][col] + prefixsum[row][col-1]
                                       - prefixsum[row-1][col-1] + matrix[row][col])

        self.prefixsum = prefixsum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.prefixsum:
            return 0

        total = self.prefixsum[row2][col2]

        if row1 > 0:
            total -= self.prefixsum[row1-1][col2]
        if col1 > 0:
            total -= self.prefixsum[row2][col1-1]
        if row1 > 0 and col1 > 0:
            total += self.prefixsum[row1-1][col1-1]

        return total


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))  # Output: 8
print(obj.sumRegion(1, 1, 2, 2))  # Output: 11
print(obj.sumRegion(1, 2, 2, 4))  # Output: 12

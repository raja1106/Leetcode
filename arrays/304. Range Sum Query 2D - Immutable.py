from typing import List
class NumMatrix: #TODOO

    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            self.prefixsum = []
            return
        m = len(matrix)
        n = len(matrix[0])

        prefixsum = [[0 for _ in range(n)] for _ in range(m)]
        prefixsum[0][0] = matrix[0][0]

        for row in range(1,m):
            prefixsum[row][0] = prefixsum[row-1][0]+matrix[row][0]
        for col in range(1,n):
            prefixsum[0][col] = prefixsum[0][col-1] + matrix[0][col]

        for row in range(1,m):
            for col in range(1,n):
                prefixsum[row][col] = (prefixsum[row-1][col] + prefixsum[row][col-1]-prefixsum[row-1][col]
                                       +matrix[0][col])

        self.prefixsum =prefixsum



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return 1

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

test = [1 for j in range(3)]
print(test)
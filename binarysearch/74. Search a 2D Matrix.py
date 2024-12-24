class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])
        start, end = 0, (rows * cols) - 1

        while start <= end:
            mid = start + (end - start) // 2
            x = mid // cols
            y = mid % cols
            #x, y = divmod(mid, n) this is another way
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                end = mid-1
            else:
                start = mid+1
        return False
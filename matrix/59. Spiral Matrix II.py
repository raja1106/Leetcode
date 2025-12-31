from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        res = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        sequence = 1
        while top <= bottom and left <= right:
            # 1) left -> right on top row
            for c in range(left, right + 1):
                res[top][c] = sequence
                sequence += 1
            top += 1

            # 2) top -> bottom on right column
            for r in range(top, bottom + 1):
                res[r][right] = sequence
                sequence += 1
            right -= 1

            # 3) right -> left on bottom row (only if still valid rows)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res[bottom][c] = sequence
                    sequence += 1
                bottom -= 1

            # 4) bottom -> top on left column (only if still valid cols)
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res[r][left] = sequence
                    sequence += 1
                left += 1

        return res


class Solution_with_more_memory:
    def generateMatrix(self, n: int) -> List[List[int]]:

        result = [[0] * n for _ in range(n)]

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        i = 0
        sequence = 1

        row, col = 0, 0
        visited = set()
        result[row][col] = 1
        visited.add((row, col))
        while sequence < (n * n):
            current_dirction = direction[i % 4]
            dr = current_dirction[0]
            dc = current_dirction[1]
            if 0 <= row + dr < n and 0 <= col + dc < n and (row + dr, col + dc) not in visited:
                sequence += 1
                row = row + dr
                col = col + dc
                result[row][col] = sequence
                visited.add((row, col))

            else:
                i += 1

        return result
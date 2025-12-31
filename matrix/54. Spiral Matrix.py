from typing import List


class Solution_Best:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        [1, 2, 3, 4]
        [5, 6, 7, 8]
        [9,10,11,12]

        """
        result = []

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        i = 0
        m = len(matrix)
        n = len(matrix[0])
        row, col = 0, 0
        visited = set()
        result.append(matrix[row][col])
        visited.add((row, col))
        while len(result) < (m * n):
            current_dirction = direction[i % 4]
            dr = current_dirction[0]
            dc = current_dirction[1]
            if 0 <= row + dr < m and 0 <= col + dc < n and (row + dr, col + dc) not in visited:
                row = row + dr
                col = col + dc
                result.append(matrix[row][col])
                visited.add((row, col))
            else:
                i += 1

        return result

from typing import List

class Solution_Optimized_for_Space:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1) left -> right on top row
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # 2) top -> bottom on right column
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # 3) right -> left on bottom row (only if still valid rows)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            # 4) bottom -> top on left column (only if still valid cols)
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        output = []

        # Directions are in the order: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_direction = 0

        row, col = 0, 0
        visited = set()

        for _ in range(m * n):
            output.append(matrix[row][col])
            visited.add((row, col))

            # Calculate next position
            next_row, next_col = row + directions[current_direction][0], col + directions[current_direction][1]

            if (0 <= next_row < m and 0 <= next_col < n and (next_row, next_col) not in visited):
                row, col = next_row, next_col
            else:
                # Change direction
                current_direction = (current_direction + 1) % 4
                row += directions[current_direction][0]
                col += directions[current_direction][1]

        return output

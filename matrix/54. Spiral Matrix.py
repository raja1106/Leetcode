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

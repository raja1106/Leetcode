from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        rows, cols = len(mat), len(mat[0])
        result = []
        direction = 1  # 1 for up-right, -1 for down-left
        row, col = 0, 0
        while len(result) < rows * cols:
            result.append(mat[row][col])
            if direction == 1:  # Moving up-right
                if col == cols - 1:  # Hit the right border
                    row += 1
                    direction = -1
                elif row == 0:  # Hit the top border
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1
            else:  # Moving down-left
                if row == rows - 1:  # Hit the bottom border
                    col += 1
                    direction = 1
                elif col == 0:  # Hit the left border
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1

        return result


def run_tests():
    test_cases = [
        ([
             [1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]
         ], [1, 2, 4, 7, 5, 3, 6, 8, 9]),
        ([
             [1, 2],
             [3, 4],
             [5, 6]
         ], [1, 2, 3, 5, 4, 6]),
        ([
             [1, 2, 3],
             [4, 5, 6]
         ], [1, 2, 4, 5, 3, 6]),
        ([
             [1, 2, 3, 4]
         ], [1, 2, 3, 4]),
        ([
             [1],
             [2],
             [3],
             [4]
         ], [1, 2, 3, 4]),
        ([], []),
        ([[42]], [42])
    ]

    solution = Solution()
    for i, (mat, expected) in enumerate(test_cases):
        result = solution.findDiagonalOrder(mat)
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed.")


run_tests()

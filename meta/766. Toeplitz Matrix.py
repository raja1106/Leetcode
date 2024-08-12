from typing import List

class Solution:
    def is_toeplitz_matrix(self, matrix: List[List[int]]) -> bool:
        """
        Check if a matrix is a Toeplitz matrix.
        A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

        :param matrix: 2D List[int], the input matrix to check
        :return: bool, True if the matrix is Toeplitz, False otherwise
        """

        # Check for empty matrix or single row/column edge cases
        if not matrix or not matrix[0]:
            return True

        row_count = len(matrix)
        col_count = len(matrix[0])

        # Iterate over each element in the matrix starting from the second row and second column
        for i in range(1, row_count):
            for j in range(1, col_count):
                # Compare the current element with the element diagonally above and to the left.
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        # If all diagonal comparisons hold, the matrix is Toeplitz.
        return True
def run_tests():
    solution = Solution()

    test_cases = [
        ([[1, 1], [1, 1]], True),
        ([[1, 2], [2, 1]], False),
        ([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]], True),
        ([[1, 2, 3, 4], [5, 1, 9, 3], [9, 5, 1, 2]], False),
        ([[1, 2, 3, 4]], True),
        ([[1], [2], [3], [4]], True),
        ([], True),
        ([[3, 8, 9], [5, 3, 8], [4, 5, 3], [2, 4, 5]], True),
        ([[0, -1, -2], [-1, 0, -1], [-2, -1, 0]], True),
        ([[7, 8, 9, 10, 11], [6, 7, 8, 9, 10], [5, 6, 7, 8, 9], [4, 5, 6, 7, 8], [3, 4, 5, 6, 7]], True)
    ]

    for i, (matrix, expected) in enumerate(test_cases):
        result = solution.is_toeplitz_matrix(matrix)
        print(f"Test Case {i+1}: {'Pass' if result == expected else 'Fail'}")

run_tests()

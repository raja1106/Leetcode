from collections import deque
from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # Edge case: empty input
        if not nums or not nums[0]:
            return []
        # Number of rows (each row may have different length)
        num_rows = len(nums)
        # Movements: down first (to increase r + c), then right
        directions = [(1, 0), (0, 1)]
        # Initialize BFS queue and seen set
        queue = deque([(0, 0)])
        seen = {(0, 0)}
        result = []
        while queue:
            r, c = queue.popleft()
            result.append(nums[r][c])
            # Enqueue down and right neighbors in BFS order
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < num_rows and 0 <= nc < len(nums[nr])and (nr, nc) not in seen):
                    seen.add((nr, nc))
                    queue.append((nr, nc))

        return result


from collections import defaultdict

class Solution_1st_Efficient:
    def findDiagonalOrder(self, nums):
        # 1) Collect into buckets keyed by (row + col)
        buckets = defaultdict(list)
        for r, row in enumerate(nums):
            for c, v in enumerate(row):
                buckets[r + c].append(v)

        # 2) Flatten in ascending diagonal order,
        #    reversing each bucket so we go bottom→top
        result = []
        for d in range(len(buckets)):
            result.extend(buckets[d][::-1])
        return result


class Solution_2:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # Initialize an empty list to store the values along with their diagonal indices
        diagonal_elements = []

        # Iterate through the matrix rows
        for row_index, row in enumerate(matrix):
            # Iterate through the elements in the current row
            for column_index, value in enumerate(row):
                # The sum of row and column indices gives the diagonal index.
                # Append a tuple containing the diagonal index, column index and the value
                diagonal_elements.append((row_index + column_index, column_index, value))

        # Sort the list of tuples based on diagonal index, then by column index (as secondary)
        # This will order the elements first by diagonal, then from top-right to bottom-left
        # within the same diagonal line.
        diagonal_elements.sort()

        # Extract the values from the sorted list of tuples and return them in the correct order
        return [element[2] for element in diagonal_elements]

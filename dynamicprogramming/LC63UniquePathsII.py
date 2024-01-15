from typing import List

def uniquePathsWithObstacles(self, obstacle_grid: List[List[int]]) -> int:
    if not obstacle_grid:
        return 0
    if obstacle_grid[0][0] == 1:
        return 0
    # Get the number of rows and columns in the obstacle grid.
    rows, cols = len(obstacle_grid), len(obstacle_grid[0])

    # Initialize the DP (Dynamic Programming) table with zeros.
    dp_table = [[0] * cols for _ in range(rows)]

    # Set the value for the first cell to 1 if it is not an obstacle.
    if obstacle_grid[0][0] == 0:
        dp_table[0][0] = 1

    # Populate the first column of the DP table.
    for i in range(1, rows):
        if obstacle_grid[i][0] == 0:  # If there is no obstacle,
            dp_table[i][0] = 1  # Use value from cell above.
        else:
            break
    # Populate the first row of the DP table.
    for j in range(1, cols):
        if obstacle_grid[0][j] == 0:  # If there is no obstacle,
            dp_table[0][j] = 1  # Use value from cell to the left.
        else:
            break
    # Fill in the rest of the DP table.
    for i in range(1, rows):
        for j in range(1, cols):
            if obstacle_grid[i][j] == 0:  # If the current cell is not an obstacle,
                dp_table[i][j] = dp_table[i - 1][j] + dp_table[i][j - 1]  # Sum of top and left cells.

    # The bottom-right cell of the DP table will hold the number of unique paths.
    return dp_table[-1][-1]
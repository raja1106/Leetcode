class Solution:#This is not working
    def isValid(self, board, row, col, num):
        # Check if we already have the same number in the same row, col or box
        for x in range(9):
            if board[row][x] == num:
                return False  # Check if the same number is in the same row
            if board[x][col] == num:
                return False  # Check if the same number is in the same col
            if board[(row // 3) * 3 + x // 3][(col // 3) * 3 + x % 3] == num:
                return False  # Check if the same number is in the same 3x3 box
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':  # If we find an empty cell
                    for num in range(1, 10):  # Try every number from 1-9
                        if self.isValid(board, row, col, str(num)):  # Check if the number is valid in the current cell
                            board[row][col] = str(num)  # If it is valid, fill the cell with the number
                            if self.solveSudoku(board):  # Recursively call the function to solve the rest of the board
                                return True
                            else:  # If the current number doesn't lead to a solution, backtrack by emptying the cell
                                board[row][col] = '.'
                    return False  # If we have tried every number and none of them lead to a solution, return false
        return True

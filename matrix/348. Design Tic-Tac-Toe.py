class TicTacToe_Optimized:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti = 0

    def move(self, row: int, col: int, player: int) -> int:  #O(1)
        add = 1 if player == 1 else -1

        self.rows[row] += add
        self.cols[col] += add

        if row == col:
            self.diag += add
        if row + col == self.n - 1:
            self.anti += add
        n = self.n
        if (abs(self.rows[row]) == n or
            abs(self.cols[col]) == n or
            abs(self.diag) == n or
            abs(self.anti) == n):
            return player
        return 0


class TicTacToe:

    def __init__(self, n: int):
        self.k = n
        self.board = [[0] * n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:#O(n)
        n = self.k
        self.board[row][col] = player

        for i in range(n):
            if self.board[i][col] != player:
                break
            if i == n - 1:
                return player

        for j in range(n):
            if self.board[row][j] != player:
                break
            if j == n - 1:
                return player

        # diagonal #1
        # top-left to bottom-right diagonal
        for i in range(n):
            if self.board[i][i] != player:
                break
            if i == n - 1:
                return player

        # diagonal #2
        # top-right to bottom-left diagonal
        for i in range(n):
            if self.board[i][n - i - 1] != player:
                break
            if i == n - 1:
                return player

        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
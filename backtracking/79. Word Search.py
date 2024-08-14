from typing import List


class Solution:
    def dfs(self, board, word, i, j, k):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
            return False
        # check if we have reached the end of the word
        if k == len(word) - 1:
            return True
        # mark the current cell as visited by replacing it with '#'
        original_char, board[i][j] = board[i][j], '#'
        # check all 4 adjacent cells recursively
        for dr, dc in directions:
            if self.dfs(board, word, i + dr, j + dc, k + 1):
                return True
        # backtrack
        board[i][j] = original_char
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                # start the search from every cell
                if board[i][j] == word[0] and self.dfs(board, word, i, j, 0):
                    return True
        return False
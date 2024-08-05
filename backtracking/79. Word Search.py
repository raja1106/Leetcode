from typing import List
class Solution:
    def dfs(self, board, word, i, j, k):
        # check if current coordinates are out of grid or the current cell doesn't match the current character of the word
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
            return False
        # check if we have reached the end of the word
        if k == len(word) - 1:
            return True
        # mark the current cell as visited by replacing it with '/'
        tmp, board[i][j] = board[i][j], '/'
        # check all 4 adjacent cells recursively
        res = self.dfs(board, word, i + 1, j, k + 1) or \
              self.dfs(board, word, i - 1, j, k + 1) or \
              self.dfs(board, word, i, j + 1, k + 1) or \
              self.dfs(board, word, i, j - 1, k + 1)
        # of if its in single line use like below instead of above 4 lines
        # res = self.dfs(board, word, i + 1, j, k + 1) or self.dfs(board, word, i - 1, j, k + 1) or self.dfs(board, word, i, j + 1, k + 1) or self.dfs(board, word, i, j - 1, k + 1)

        # backtrack by replacing the current cell with its original value
        board[i][j] = tmp
        return res
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                # start the search from every cell
                if self.dfs(board, word, i, j, 0):
                    return True
        return False

def main():
  sol = Solution()
  # Test Case 1
  board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
  ]
  word = "ABCCED"
  print(sol.exist(board, word)) # expected output: True

  # Test Case 2
  board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
  ]
  word = "SEE"
  print(sol.exist(board, word)) # expected output: True

  # Test Case 3
  board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
  ]
  word = "ABCB"
  print(sol.exist(board, word)) # expected output: False

  # Test Case 4
  board = [['a','a']]
  word = "aaa"
  print(sol.exist(board, word)) # expected output: False

  # Test Case 5
  board = [['a']]
  word = "a"
  print(sol.exist(board, word)) # expected output: True

  # Test Case 6
  board = [
      ['a','b','c','d','e'],
      ['f','g','h','i','j'],
      ['k','l','m','n','o'],
      ['p','q','r','s','t'],
      ['u','v','w','x','y'],
      ['z','a','b','c','d']
  ]
  word = "abcde"
  print(sol.exist(board, word)) # expected output: True

  # Test Case 7
  board = [
      ['a','b','c','d','e'],
      ['f','g','h','i','j'],
      ['k','l','m','n','o'],
      ['p','q','r','s','t'],
      ['u','v','w','x','y'],
      ['z','a','b','c','d']
  ]
  word = "zabcd"
  print(sol.exist(board, word)) # expected output: True

main()
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(word1) and j == len(word2):
                return 0

            if i == len(word1):
                return len(word2) - j

            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
            else:
                option1 = 2 + dfs(i + 1, j + 1)
                option2 = 1 + dfs(i + 1, j)
                option3 = 1 + dfs(i, j + 1)
                memo[(i, j)] = min(option1, option2, option3)
                return memo[(i, j)]

        return dfs(0, 0)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Input: word1 = "sea", word2 = "eat"
        optimization problem

        """
        memo = {}
        def lcs_seq(i,j):
            if i == len(word1) or j == len(word2):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            max_val = 0
            if word1[i] == word2[j]:
                max_val = 1+lcs_seq(i+1,j+1)
            max_val = max(max_val,lcs_seq(i+1,j),lcs_seq(i,j+1))
            memo[(i,j)] = max_val
            return memo[(i,j)]
        max_lcs_seq = lcs_seq(0,0)
        return (len(word1)-max_lcs_seq)+(len(word2)-max_lcs_seq)



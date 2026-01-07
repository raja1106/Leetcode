from typing import List
from typing import List


class Solution_Topdown_Best:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            # If we've already calculated results for this suffix, return them
            if start in memo:
                return memo[start]
            res = []
            # Base case: reached the end of the string
            if start == len(s):
                res.append("")
                return res

            # Try every possible end position for a word starting at 'start'
            for end in range(start, len(s)):
                word = s[start:end + 1]

                if word in word_set:
                    # Get all possible completions for the rest of the string
                    sub_sentences = dfs(end + 1)

                    for sub in sub_sentences:
                        # If sub is empty (base case), just add the word
                        # Otherwise, join word and sub-sentence with a space
                        sentence = word + ("" if sub == "" else " " + sub)
                        res.append(sentence)

            memo[start] = res
            return res

        return dfs(0)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dict_set = set(wordDict)
        n = len(s)
        dp = [[] for _ in range(n + 1)]  # dp[i] will store all sentences formed by s[0:i]
        dp[0] = [""]  # Base case: There's one way to form an empty string

        for end in range(1, n + 1):
            for start in range(end):
                word = s[start:end]
                if word in dict_set:
                    for sentence in dp[start]:
                        if sentence:
                            dp[end].append(sentence + " " + word)
                        else:
                            dp[end].append(word)

        return dp[n]


class Solution_bruteforce:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        dict_set = set(wordDict)

        def dfs(i, slate):
            if i == len(s):
                result.append(' '.join(slate))
                return
            for end in range(i + 1, len(s) + 1):
                if s[i:end] in dict_set:
                    slate.append(s[i:end])
                    dfs(end, slate)
                    slate.pop()

        dfs(0, [])
        return result
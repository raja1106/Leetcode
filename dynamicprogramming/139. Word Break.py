from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for end in range(1, n + 1):
            for start in range(end):
                if dp[start] and s[start:end] in dict_set:
                    dp[end] = True
                    break

        return dp[n]


class Solution_mine:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # empty substring can always be segmented

        for i in range(1, len(s) + 1):
            j = i - 1

            while j >= 0:
                if s[j:i] in dict_set and dp[j] == True:
                    dp[i] = True
                    break
                j -= 1

        return dp[n]

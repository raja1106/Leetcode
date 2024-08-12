from typing import List

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
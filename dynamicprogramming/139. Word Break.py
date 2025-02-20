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


from typing import List


class Solution_Bruteforce:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(start):
            # Base Case: If we've checked all characters, return True
            if start == len(s):
                return True

            # Try every possible prefix
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict and dfs(end):  # If valid word found, recurse
                    return True

            return False

        return dfs(0)


class Solution_Memoization:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Determines if the given string `s` can be segmented into a space-separated sequence
        of one or more dictionary words from `wordDict`.

        Args:
        - s (str): The input string to segment.
        - wordDict (List[str]): The list of valid words.

        Returns:
        - bool: True if `s` can be segmented into words from `wordDict`, otherwise False.
        """
        memo = {}  # Memoization dictionary to store computed results

        def dfs(start: int) -> bool:
            """
            Recursively checks if the substring `s[start:]` can be broken into valid words.

            Args:
            - start (int): The starting index of the current substring being checked.

            Returns:
            - bool: True if `s[start:]` can be segmented, otherwise False.
            """

            # Base Case: If we've checked all characters, return True
            if start == len(s):
                return True

            # Check memoization to avoid redundant computations
            if start in memo:
                return memo[start]

            # Try every possible prefix `s[start:end]`
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict:  # If this prefix is a valid word
                    if dfs(end):  # Recursively check the remaining substring
                        memo[start] = True  # Cache the result (successful segmentation)
                        return True

            memo[start] = False  # Cache the result (unsuccessful segmentation)
            return False

        return dfs(0)  # Start checking from index 0

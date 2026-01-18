from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 1. Build the Trie
        root = TrieNode()
        for word in wordDict:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True

        memo = {}

        def dfs(start: int) -> bool:
            if start == len(s):
                return True
            if start in memo:
                return memo[start]

            # 2. Walk the Trie instead of slicing the string
            node = root
            for end in range(start, len(s)):
                char = s[end]
                if char not in node.children:
                    # No word in the dictionary starts with this prefix
                    break

                node = node.children[char]
                if node.is_word:
                    # Found a valid word, try recursing from the next character
                    if dfs(end + 1):
                        memo[start] = True
                        return True

            memo[start] = False
            return False

        return dfs(0)
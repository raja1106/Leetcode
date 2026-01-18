from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Build the Trie
        root = TrieNode()
        for word in wordDict:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True

        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]

            res = []
            node = root
            # Instead of slicing, we traverse the Trie character by character
            for end in range(start, len(s)):
                char = s[end]
                if char not in node.children:
                    break  # Optimization: No word starts with this prefix

                node = node.children[char]
                if node.is_word:
                    word = s[start:end + 1]
                    sub_sentences = dfs(end + 1)
                    for sub in sub_sentences:
                        res.append(word + ("" if sub == "" else " " + sub))

            memo[start] = res
            return res

        return dfs(0)
class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.isEnd = False  # Flag to represent end of a word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Inserts a word into the trie.
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True  # Mark the end of the word


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Build trie from the dictionary words
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        n = len(s)
        # dp[i] = minimum extra characters needed for s[i:]
        dp = [0] * (n + 1)
        # dp[n] = 0  # Base case: no extra characters needed for an empty string

        # Process the string from right to left
        for i in range(n - 1, -1, -1):
            # Option 1: Delete the current character
            dp[i] = 1 + dp[i + 1]

            # Option 2: Try to match dictionary words starting at index i using the Trie
            node = trie.root
            for j in range(i, n):
                if s[j] not in node.children:
                    break  # No further match possible in the Trie
                node = node.children[s[j]]
                if node.isEnd:
                    # If a valid word ends at position j, update dp[i]
                    dp[i] = min(dp[i], dp[j + 1])
        return dp[0]
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

    # Returns if the word is in the trie.
    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isEnd  # Check if it's the end of a word

    # Returns if there is any word in the trie that starts with the given prefix.
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:  # Fix variable name
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True  # If we reached here, prefix exists


# Example Usage
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # True
print(trie.search("app"))  # False
print(trie.startsWith("app"))  # True
trie.insert("app")
print(trie.search("app"))  # True

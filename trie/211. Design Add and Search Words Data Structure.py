class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:#Trie
    def __init__(self):
        self.root = TrieNode()
        # Remove the following line if you do not want the empty string to be a valid word.
        # self.root.is_end = True

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, index: int) -> bool:
            # If we have reached the end of the word, check is_end flag.
            if index == len(word):
                return node.is_end

            ch = word[index]
            if ch == '.':
                # Try every possible child
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False  # No path matched.
            else:
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], index + 1)

        return dfs(self.root, 0)
